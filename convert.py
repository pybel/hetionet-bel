# -*- coding: utf-8 -*-

"""Export Hetionet in several BEL formats.

Before running this script, make sure you're on Python 3.5+
and run ``pip install "pybel==0.14.5"
"""

import os

import click
from pybel import get_hetionet, to_bel_script_gz, to_graphdati_gz, to_nodelink_gz


@click.command()
@click.option('--directory', default=os.getcwd(), type=click.Path(dir_okay=True, file_okay=False))
def main(directory: str):
    """Export Hetionet in several BEL formats."""
    click.echo('Getting hetionet')
    graph = get_hetionet()

    click.echo('Exporting BEL Script')
    script_gz_path = os.path.join(directory, 'hetionet-v1.0.bel.gz')
    to_bel_script_gz(graph, script_gz_path)

    click.echo('Exporting Nodelink')
    nodelink_gz_path = os.path.join(directory, 'hetionet-v1.0.bel.nodelink.json.gz')
    to_nodelink_gz(graph, nodelink_gz_path)

    click.echo('Exporting GraphDati')
    graphdati_gz_path = os.path.join(directory, 'hetionet-v1.0.bel.graphdati.json.gz')
    to_graphdati_gz(graph, graphdati_gz_path)


if __name__ == '__main__':
    main()
