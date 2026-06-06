class PluginBase:
    def process(self, frame):
        """
        Every addon MUST implement this.
        Input: frame (numpy array)
        Output: processed frame
        """
        raise NotImplementedError