import pandas as pd
from mayavi import mlab


def main():
    df = pd.read_csv('data/sup_brown.xyz', header=None, sep=' ', decimal=',', names=['x', 'y', 'z', 'n'])
    df = df[['x', 'y', 'z']]
    X_bmf = df['x'].values
    Y_bmf = df['y'].values
    Z_bmf = df['z'].values
    mlab.clf()
    fig3d = mlab.figure(1, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
    # Visualize the points
    pts = mlab.points3d(X_bmf, Y_bmf, Z_bmf, Z_bmf,
                        scale_mode='none', scale_factor=0.02)

    # Create and visualize the mesh
    mesh = mlab.pipeline.delaunay2d(pts)
    surf = mlab.pipeline.surface(mesh, colormap='Spectral')

    mlab.show()

if __name__ == '__main__':
    main()
