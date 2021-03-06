from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np
import pandas as pd

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 200)

from aiflearn.datasets import AdultDataset
from aiflearn.datasets import BankDataset
from aiflearn.datasets import CompasDataset
from aiflearn.datasets import GermanDataset
from aiflearn.metrics import BinaryLabelDatasetMetric


def test_compas():
    # just test that there are no errors for default loading...
    cd = CompasDataset()
    # print(cd)

def test_german():
    gd = GermanDataset()
    bldm = BinaryLabelDatasetMetric(gd)
    assert bldm.num_instances() == 1000

def test_adult_test_set():
    ad = AdultDataset()
    # train, test = ad.split([32561])
    train, test = ad.split([30162])
    assert np.any(test.labels)

def test_adult():
    ad = AdultDataset()
    # print(ad.feature_names)
    assert np.isclose(ad.labels.mean(), 0.2478, atol=5e-5)

    bldm = BinaryLabelDatasetMetric(ad)
    assert bldm.num_instances() == 45222

def test_adult_no_drop():
    ad = AdultDataset(protected_attribute_names=['sex'],
        privileged_classes=[['Male']], categorical_features=[],
        features_to_keep=['age', 'education-num'])
    bldm = BinaryLabelDatasetMetric(ad)
    assert bldm.num_instances() == 48842
