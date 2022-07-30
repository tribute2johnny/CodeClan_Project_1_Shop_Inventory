from bdb import set_trace
import pdb
from models.spaceship import Spaceship
from models.manufacturer import Manufacturer

import repositories.spaceship_repository as spaceship_repository
import repositories.manufacturer_repository as manufacturer_repository


manufacturer_repository.select_all()
manufacturer_repository.delete_all()

# creates some base data for manufacturers


manufacturer_1 = Manufacturer("Faulcon DeLacy", "Faulcon DeLacy is an independent manufacturer of ships and equipment. They specialize in producing multipurpose and combat-oriented ships.")
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer("Core Dynamics", "Core Dynamics specializes in producing high-performance combat ships, and is the primary supplier of ships for the Federal Navy.")
manufacturer_repository.save(manufacturer_2)

manufacturer_3 = Manufacturer("Gautemaya", "Gutamaya, also known as Imperial Gutamaya, is an Imperial manufacturer of ships and various equipment. It specialises in producing combat and multipurpose ships known for their sleek, elegant designs, and is the primary supplier of ships for the Imperial Navy.")
manufacturer_repository.save(manufacturer_3)

manufacturer_4 = Manufacturer("Lakon Spaceways", "Lakon Spaceways is an Allied manufacturer of ships. It specialises in producing durable, utilitarian freighters and exploration vessels.")
manufacturer_repository.save(manufacturer_4)

manufacturer_5 = Manufacturer("Zorgon Peterson", "Zorgon Peterson is an independent manufacturer of ships and equipment in the galaxy. It produces a small yet eclectic range of ships, including small freighters and high-performance combat craft.")
manufacturer_repository.save(manufacturer_5)

manufacturer_6 = Manufacturer("Saud Kruger", "Saud Kruger is an independent corporation based in Bedaho that manufactures luxury passenger ships and equipment for the wealthy in the galaxy.")
manufacturer_repository.save(manufacturer_6)



spaceship_repository.select_all()
spaceship_repository.delete_all()

#creates some base data for spaceships

spaceship_1 = Spaceship("Vulture", "Fighter", manufacturer_2,  "The Vulture is a ship manufactured by Core Dynamics. The Vulture primarily serves as a heavy space-superiority fighter.", 3, 400600, 623000)
spaceship_repository.save(spaceship_1)

spaceship_2 = Spaceship("Fer De Lance", "Fighter", manufacturer_5, "The Fer-de-Lance is a heavy combat ship manufactured by Zorgon Peterson. It features a hull that is more resistant to damage from weapons than other medium ships.", 6, 700500, 988000)
spaceship_repository.save(spaceship_2)

spaceship_3 = Spaceship("Type-9 Heavy", "Freighter", manufacturer_4, "The Type-9 Heavy is a ship manufactured by Lakon Spaceways. It is the largest of Lakon's five freighter models, as well as the largest dedicated trading ship.", 12, 1200000, 1700000)
spaceship_repository.save(spaceship_3)

spaceship_4 = Spaceship("Diamondback", "Explorer", manufacturer_4, "The Diamondback Explorer manufactured by Lakon Spaceways is a dual-role ship designed with both exploration and combat in mind.", 0, 120000, 200000)
spaceship_repository.save(spaceship_4)

spaceship_5 = Spaceship("Imperial Cutter", "Multipurpose", manufacturer_3, "The Imperial Cutter is a ship manufactured by Gutamaya for the Empire. It serves as the Imperial Navy's primary transport ship.", 2, 540000, 770000)
spaceship_repository.save(spaceship_5)

spaceship_6 = Spaceship("Asp Explorer", "Explorer", manufacturer_4, "The Asp Explorer is a ship manufactured by Lakon Spaceways. Agile, well-armed for its size, and capable of achieving high jump ranges.", 7, 340000, 450000)
spaceship_repository.save(spaceship_6)

spaceship_7 = Spaceship("Cobra MkIII", "Multipurpose", manufacturer_1, "The Cobra MkIII is a multipurpose ship manufactured by Faulcon DeLacy. A time-honoured and well-respected design.", 20, 100000, 145000)
spaceship_repository.save(spaceship_7)

spaceship_8 = Spaceship("Python", "Multipurpose", manufacturer_1, "The Python is a ship manufactured by Faulcon DeLacy. An iconic model, the Python pioneered modular ship design and singlehandedly revolutionized space travel.", 0, 850000, 999000)
spaceship_repository.save(spaceship_8)

spaceship_9 = Spaceship("Type-7 Transporter", "Freighter", manufacturer_4, "The Type-7 Transporter is a ship manufactured by Lakon Spaceways. A dedicated freighter with a classic design.", 1, 520000, 610000)
spaceship_repository.save(spaceship_9)

spaceship_10 = Spaceship("Adder", "Multipurpose", manufacturer_5, "The Adder is a ship manufactured by Zorgon Peterson. The Adder is a small multipurpose ship known for its sturdiness and reliability.", 3, 120000, 155000)
spaceship_repository.save(spaceship_10)






#prints all space ships to the terminal, tests the data and select all function.

# result = spaceship_repository.select_all()

# for spaceship in result:
#     print(spaceship.__dict__)





# pdb.set_trace()