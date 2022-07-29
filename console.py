from bdb import set_trace
import pdb
from models.spaceship import Spaceship
from models.manufacturer import Manufacturer

import repositories.spaceship_repository as spaceship_repository
import repositories.manufacturer_repository as manufacturer_repository



manufacturer_1 = Manufacturer("Faulcon DeLacy", "Faulcon DeLacy is an independent manufacturer of ships and equipment. They specialize in producing multipurpose and combat-oriented ships.")
manufacturer_repository.save(manufacturer_1)














pdb.set_trace()