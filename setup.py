from setuptools import setup

setup(
    entry_points={
        "spey.backend.plugins": [
            "contur.full_histogram_likelihood = contur_likelihood:ConturHistogram"
        ]
    }
)