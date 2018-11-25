#!/usr/bin/env python3

import argparse
import requests
import sys


def parse_cli():
    """Parse the args"""
    parser = argparse.ArgumentParser()

    parser.add_argument("postcode",
        help="Postal code to look up.")

    parser.add_argument("--country", default="gb",
        help="Country code for where to look up postcode.")

    args = parser.parse_args()

    return args


def _make_postcodes_io_request(postcode, extra_path='', retries=0):
    """Make request to postcodes.io with single retry on timeout."""
    url_base = 'https://api.postcodes.io/postcodes'
    url = "{base}/{postcode}{extra}".format(
        base=url_base,
        postcode=postcode,
        extra=extra_path
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(e)
        sys.exit(1)
    except requests.exceptions.Timeout:
        # Going to retry once
        if retries == 0:
            _make_postcodes_io_request(postcode, extra_path, 1)
        else:
            print("timeout on {url}".format(url=url))
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def is_postcode_valid(postcode):
    """Check a postcode for validity"""
    res = _make_postcodes_io_request(postcode, '/validate')
    return res.get('result', False)


def _filter_country_region(postcode_data):
    """Filter down to just country and region data"""
    return {
        "postcode": postcode_data.get('postcode', ''),
        "country": postcode_data.get('country', 'Unknown'),
        "region": postcode_data.get('region', 'Unknown'),
    }


def get_postcode_info(postcode):
    """Get postcode general information"""
    res = _make_postcodes_io_request(postcode)
    return _filter_country_region(res.get('result', {}))


def get_nearest_postcodes_list(postcode):
    """Get nearest postcodes list with country and region"""
    res = _make_postcodes_io_request(postcode, '/nearest')
    nearest = []
    for info in res.get('result', []):
        nearby = _filter_country_region(info)
        nearest.append(nearby)

    return nearest


def main():
    args = parse_cli()

    # validate the postcode
    if not is_postcode_valid(args.postcode):
        print("Postcode '{}' is invalid".format(args.postcode))
    else:
        print("Postcode '{}' is valid".format(args.postcode))

    # print postcode info
    info = get_postcode_info(args.postcode)
    print("Postcode '{code}' is from country {country} and region {region}".format(
        code=args.postcode,
        country=info["country"],
        region=info["region"],)
    )

    # print nearest postcodes list
    nearest = get_nearest_postcodes_list(args.postcode)
    if len(nearest) > 0:
        print("Nearby postcodes are:")
        for nearby in nearest:
            print("{code} - {country} - {region}".format(
                code=nearby["postcode"],
                country=nearby["country"],
                region=nearby["region"],)
            )
    else:
        print("Found no nearby postcodes")


if __name__ == "__main__":
    main()
