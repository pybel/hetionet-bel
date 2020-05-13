# -*- coding: utf-8 -*-

"""Export Hetionet in several BEL formats.

Before running this script, make sure you're on Python 3.5+
and run ``pip install pybel``.
"""

import gzip
import os

import click
from pyobo.cli_utils import verbose_option

import pybel
import pybel.grounding


@click.command()
@click.option('--directory', default=os.getcwd(), type=click.Path(dir_okay=True, file_okay=False))
@verbose_option
def main(directory: str):
    """Export Hetionet in several BEL formats."""
    click.echo(f'Using PyBEL v{pybel.get_version(with_git_hash=True)}')

    click.echo('Getting hetionet')
    graph = pybel.get_hetionet()

    click.echo('Grounding hetionet')
    graph = pybel.grounding.ground(graph)

    click.echo('Exporting BEL Script')
    script_gz_path = os.path.join(directory, 'hetionet-v1.0.bel.gz')
    pybel.to_bel_script_gz(graph, script_gz_path)

    click.echo('Exporting Nodelink')
    nodelink_gz_path = os.path.join(directory, 'hetionet-v1.0.bel.nodelink.json.gz')
    pybel.to_nodelink_gz(graph, nodelink_gz_path)

    click.echo('Exporting GraphDati')
    graphdati_gz_path = os.path.join(directory, 'hetionet-v1.0.bel.graphdati.json.gz')
    pybel.to_graphdati_gz(graph, graphdati_gz_path)

    click.echo('Exporting Machine Learning-ready TSV')
    tsv_path = os.path.join(directory, 'hetionet-v1.0.tsv.gz')
    with gzip.open(tsv_path, 'wt') as file:
        pybel.to_tsv(graph, file)


if __name__ == '__main__':
    main()
