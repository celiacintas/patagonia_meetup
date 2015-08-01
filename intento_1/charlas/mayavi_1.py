from mayavi import mlab
import pandas as pd


def main():

    df = pd.read_csv('data/cloudfilter.pcd', skiprows=11, sep=' ', header=None, names=['x', 'y', 'z'])
    df_not_nan = df.dropna()
    X = df_not_nan['x']
    Y = df_not_nan['y']
    Z = df_not_nan['z']

    mlab.figure(1, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))

    pts = mlab.points3d(X, Y, Z, Z, scale_mode='none', scale_factor=0.02)

    mlab.view(90)
    mlab.show()

if __name__ == '__main__':
    main()
