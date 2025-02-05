"""Filters correlated rules."""
from random import sample
from iguanas.rule_selection._base_filter import _BaseFilter
from iguanas.correlation_reduction import AgglomerativeClusteringReducer
from iguanas.utils.typing import PandasDataFrameType


class CorrelatedFilter(_BaseFilter):
    """
    Filters correlated rules based on a correlation reduction class (see the
    `correlation_reduction` sub-package).

    Parameters
    ----------
    correlation_reduction_class : AgglomerativeClusteringReducer
        Instatiated class from the `correlation_reduction` sub-package.    

    Attributes
    ----------
    rules_to_keep : List[str]
        List of rules which remain after correlated rules have been removed.
    """

    def __init__(self,
                 correlation_reduction_class: AgglomerativeClusteringReducer):

        self.correlation_reduction_class = correlation_reduction_class
        _BaseFilter.__init__(self, rules_to_keep=[])

    def fit(self,
            X_rules: PandasDataFrameType,
            y=None,
            sample_weight=None) -> None:
        """
        Calculates the uncorrelated rules(using the correlation reduction
        class).

        Parameters
        ----------
        X_rules : PandasDataFrameType
            The binary columns of the rules applied to a dataset.
        y : PandasSeriesType
            Target (if available). Only used in the method/function passed to 
            the `metric` parameter in the `correlation_reduction_class`.
        sample_weight : None
            Row-wise weights to apply (if available). Only used in the 
            method/function passed to the `metric` parameter in the 
            `correlation_reduction_class`.  
        """

        self.correlation_reduction_class.fit(
            X=X_rules, y=y, sample_weight=sample_weight
        )
        self.rules_to_keep = self.correlation_reduction_class.columns_to_keep
