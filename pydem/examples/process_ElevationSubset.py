if __name__ == "__main__":
    import os
    from pydem.processing_manager import ProcessManager
    path = r'/home/ubuntu/data/elevation_subset'

    #from pydem.utils import rename_files
    #elev_source_files = [os.path.join(path, fn)
    #                              for fn in os.listdir(path)
    #                              if os.path.splitext(fn)[-1]
    #                              in ['.tif', '.tiff']]
    #rename_files(elev_source_files)

    savepath = os.path.join('/home', 'ubuntu', 'data', 'processed_data')
    pm = ProcessManager(path, savepath)
    pm._DEBUG = True
    pm.process()
