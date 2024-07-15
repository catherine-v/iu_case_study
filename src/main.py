import argparse
from extract import get_products
from load import load


DEAFULT_PRODUCT_IDS: list[str] = [
    "737628064502",
    "3017620422003",
    "5449000131805",
    "3175680011534",
    "8000500310427",
    "3228857000166",
    "3229820782560",
    "5410188031072",
    "5010477348630",
    "3068320114453",
    "3088543506255",
    "3033490506629",
    "7622210476104",
    "5000112611878",
    "3228021170022",
    "5411188119098",
    "3073781115345",
    "3252210390014",
    "20724696",
    "8076809513753",
    "87157239",
    "7622300441937",
    "5053990156009",
    "20916435",
]


class SplitArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values.split(","))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--product_ids",
        help="Comma-separated list of product ids",
        action=SplitArgs,
        default=DEAFULT_PRODUCT_IDS,
    )
    parser.add_argument(
        "--conn_str",
        help="Connection string to the database",
        default="postgresql://example:example@db:5432/example",
    )
    args = parser.parse_args()

    products = []
    for product in get_products(args.product_ids):
        products.append(product)

    load(products, args.conn_str)
