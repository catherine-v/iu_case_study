from typing import Generator, Any
import logging

import openfoodfacts
from pydantic import ValidationError

from schemas import ProductSchema


FIELDS_TO_FETCH = [
    "id",
    "categories_hierarchy",
    "generic_name",
    "nutriscore_score",
    "quantity",
    "origins",
    "allergens",
]


logger = logging.getLogger(__name__)
api = openfoodfacts.API(user_agent="IUCaseStudy/1.0")


def get_products(product_ids: list[str]) -> Generator[ProductSchema, None, None]:
    """
    Get products from the Open Food Facts API.

    :param product_ids: List of product ids
    :return: Generator of ProductSchema objects
    """
    for product_id in product_ids:
        result = api.product.get(product_id, fields=FIELDS_TO_FETCH)
        try:
            yield ProductSchema(**result)
        except ValidationError as e:
            logger.error("ERROR parsing an API response: %s", e.errors())
