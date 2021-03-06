from astropy.io import registry
from data_objects import CubeData
from astropy.wcs import WCS
from astropy.nddata import StdDevUncertainty
import astropy.units as u


def fits_cube_reader(filename):
    from astropy.io import fits
    hdulist = fits.open(filename)

    return CubeData(hdulist[1].data,
                    uncertainty=StdDevUncertainty(hdulist[3].data),
                    mask=hdulist[2].data.astype(int),
                    wcs=WCS(hdulist[0].header),
                    unit=u.Jy / u.Angstrom)


def fits_identify(origin, *args, **kwargs):
    return isinstance(args[0], basestring) and \
           args[0].lower().split('.')[-1] in ['fits', 'fit']


registry.register_reader('fits', CubeData, fits_cube_reader)
registry.register_identifier('fits', CubeData, fits_identify)