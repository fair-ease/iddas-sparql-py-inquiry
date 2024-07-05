from pykg2tbl import DefaultSparqlBuilder, KGSource, QueryResult
from pathlib import Path
from pandas import DataFrame


# SPARQL EndPoint to use - wrapped as Knowledge-Graph 'source'
IDDAS_ENDPOINT: str = "https://fair-ease-iddas.maris.nl/sparql/query"
IDDAS:KGSource = KGSource.build(IDDAS_ENDPOINT)

TEMPLATES_FOLDER = str(Path().absolute())
GENERATOR = DefaultSparqlBuilder(templates_folder=TEMPLATES_FOLDER)


def generate_sparql(name: str, **vars) -> str: 
    """ Simply build the sparql by using the named query and applying the vars
    """
    return GENERATOR.build_syntax(name, **vars)


def execute_to_df(name: str, **vars) -> DataFrame:
    """ Builds the sparql and executes, returning the result as a dataframe.
    """
    sparql = generate_sparql(name, **vars)
    result: QueryResult = IDDAS.query(sparql=sparql)
    return result.to_dataframe()
