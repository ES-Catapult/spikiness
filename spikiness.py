from numpy import float64
import numpy as np
import pandas as pd


def spikiness(data: pd.Series) -> float64:
    """Calculate spikiness for a pandas data Series. 
    The basis of this calculation is the spikiness function:
    int( (y''(t))**2 )dt - The integral of the square of the second derivative of the function
    Here we calculate the RMS spikiness for evenly spaced data

    Args:
        data (pd.Series): The pandas Series for which spikiness will be evaluated

    Returns:
        float64: The spikiness calculated for data
    """
    # Normalize the data so we calculate spikiness only (not influenced by size of values in data)
    y = data / data.abs().mean()

    y_dd = y.diff().diff()
    y_dd_sqrd = y_dd ** 2

    # Use fillna(0) so that mean is taken over the full number of original points
    spikiness = np.sqrt(y_dd_sqrd.fillna(0).mean())

    return spikiness
