from scipy import signal
# todo proceed here and we need to check what resampling does to the data.

class DepthSampler:
    """
    Resamples a video from any size of timesteps to the given size
    """

    def __init__(self, size):
        """
        Initiate sampler with the size to resample to
        :param size: int
        """
        self.size = size

    def __call__(self, x):
        """
        Uses scipy signal resample function to downsample/upsample the signal to the given size
        :param x: ndarray
        :return: ndarray
        """
        return signal.resample(x, self.size, axis=0)


class FilterDimensions:
    """
    Returns specific dimensions from the input data
    """

    def __init__(self, dims):
        self.dims = dims

    def __call__(self, x):
        """
        Returns specific dimensions from the input data
        :param x: ndarray
        :return: ndarray
        """
        return x[:, self.dims]


class Flatten:
    """
    Flattens a multi dimensional signal
    """

    def __call__(self, x):
        return x.flatten()
