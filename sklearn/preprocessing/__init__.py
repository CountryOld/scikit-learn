"""
The :mod:`sklearn.preprocessing` module includes scaling, centering,
normalization, binarization and imputation methods.
"""

from .function_transformer import FunctionTransformer

from .data import Binarizer
from .data import KernelCenterer
from .data import MinMaxScaler
from .data import Normalizer
from .data import RobustScaler
from .data import StandardScaler
from .data import add_dummy_feature
from .data import binarize
from .data import normalize
from .data import scale
from .data import robust_scale
from .data import OneHotEncoder

from .data import PolynomialFeatures

from .label import label_binarize
from .label import LabelBinarizer
from .label import LabelEncoder
from .label import MultiLabelBinarizer

from .imputation import Imputer


__all__ = [
    'Binarizer',
    'FunctionTransformer',
    'Imputer',
    'KernelCenterer',
    'LabelBinarizer',
    'LabelEncoder',
    'MinMaxScaler',
    'MultiLabelBinarizer',
    'Normalizer',
    'OneHotEncoder',
    'PolynomialFeatures',
    'RobustScaler',
    'StandardScaler',
    'add_dummy_feature',
    'binarize',
    'label_binarize',
    'normalize',
    'robust_scale',
    'scale',
]
