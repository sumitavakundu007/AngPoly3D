# AngPoly3D

AngPoly3D is a Python package to calculate the angle between a reference orientation and a polyhedron orientation considering the polyhedron's point group symmetry.

The calculated angle is the minimum of all angles after applying all the equivalent orientations on the orientation of a polyhedron according to the formula prescribed in the [paper](https://pubs.rsc.org/en/content/articlehtml/2019/sm/c8sm02643b) by Sharon C. Glotzer et al.

Orientation of a polyhedron must be provided in [quaternion](https://en.wikipedia.org/wiki/Quaternion) format.

## Contributor
- [Sumitava Kundu](https://github.com/sumitavakundu007/), [IACS, Kolkata](http://www.iacs.res.in/).

## Installation
### Prerequisites
1. [python3 or higher](https://www.python.org/download/releases/3.0/)
2. [python3-numpy](https://numpy.org/)
3. [rowan](https://rowan.readthedocs.io/en/latest/)

#### Using PyPI
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install AngPoly3D.

```bash
pip install AngPoly3D
```

#### Using source code
```bash
git clone https://github.com/sumitavakundu007/AngPoly3D.git
tar -xvf AngPoly3D-X.X.X
cd AngPoly3D-X.X.X
python3 setup.py install --user
```

## Usage

```python
from AngPoly3D import ang_poly3d_func
angles = ang_poly3d_func()
print(angles)
```
#### It will ask for few inputs to calculate the angles. You must provide the orientations, equivalent orientations and reference orientation in JSON format as following.

## sample_orientations.json
```bash
{
    "orientations": [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
}
```

## sample_equivalent_orientations.json
```bash
{
    "equiv_orientations": [[1, 0, 0, 0]]
}
```
## sample_reference_orientation.json
```bash
{
    "ref_orientation": [1, 0, 0, 0]
}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/
