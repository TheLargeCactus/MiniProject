import random
import sys
import tkinter as tk

#from QuestionDisplayer import QuestionDisplayer
#from CorrectDisplay import CorrectDisplay
#from WrongDisplay import WrongDisplay
#from EndLevelScreen import EndLevelScreen
from Planet import Planet
from Question import Question

questions = [
    Question("How big is Mercury?", "A bit bigger than a roller coaster", "Almost as a big as Earth",
             "Slightly taller than a bear", "A bit bigger than Earth's moon"),
    Question("Mercury is the second __________ planet in the solar system with Earth being the first.", "Smallest", "Coldest", "Fastest", "Densest", ),
    Question("How hot does the sunny side of Mercury get?", "2 degrees", "30 degrees", "500 degrees", "800 degrees"),
    Question("Which is true about Mercury?", "Mecrury is coldest planet in our solar system",
             " Mercury only part of our solar system on weekends", "Mercury is covered in chocolate sauce",
             "Mercury is the smallest classifield planet in the solar system"),
    Question("Mercury’s extreme temperatures are due to its lack of atmosphere and ____________ .", "Orbital speed", "Cold, metal core", "Size","Nearness to the sun"),
    Question("Why is Mercury’s magnetic field so weak? ", "Because it has a very thin atmosphere", "Because it has a very thin atmosphere","Because it orbits so quickly","Because Mercury is very small"),
    Question("If you weigh 18 pounds on Mercury how many pounds would you weigh on Earth? ", "18", "9","36","90"),
    Question("What do comets and meteors do after entering Mercury’s atmosphere? ", "Bounce out into space","Burn up", "Slow down and stay in orbit", "Slam into the planet"),
    Question("What is planet Mercury named after?", "A Heavy metal singer", "A Greek God", "The Liquid metal Mercury", "A Roman God"),
    Question("What type of planet is Mercury","Gas", "Dwarf","Liquid", "Solid"),
    Question("Venus rotates ________ than Earth.", "Faster", "Slower", "Same", "Opposite direction"),
    Question("Venus has over 10,000 ___________. ", "Tourist", "Ice Cream bars", "KitKat", "Volcanoes"),
    Question("How hot is the surface of Venus? ", "It's not even hot", "Somewhat", "100 degrees",
             "900 degress or more"),
    Question("Venus is roughly the same size as ____________. ", "Disneyland", "My backyard", "United States", "Earth"),
    Question("Who is the planet Venus named after? ", "Walt Disney", "Pokemon Creator", "Elon Musk",
             "The Roman goddess of Love"),
    Question("What lies thick on the surface of Venus?", "Ice Cream", "Yogurt", "Gum", "Carbon Dioxide"),
    Question("What is Venus sometimes called?", "Mother Russsia", "Maple leaf", "Mr.Freeze",
             " Morning or evening star"),
    Question("117 days on Earth are how many days on Venus? ", "200", "1,000", "10,000", "1"),
    Question("What is a comet made of? ", "water", "Sand and Rocks", "Candy", "Ice"),
    Question("Which of the following states of matter has a definite shape?", "liquid", "Gas", "Heat", "Solid"),
    Question("A thermometer measures", "Water", "Light", "Height", "Temperature"),
    Question("The sun is made of ______ gases. ", "Farting", "Helium and neon", "Neon", "Hydrogen and Helium"),
    Question("What is the sun?", "Planet", "Giant planet", "Asteroid", "Star"),
    Question("Which celestial body has the most gravitational pull?", "Earth", "Moon", "Asteroid", "Sun"),
    Question("What two forces keep Earth in orbit with the sun?", "Heat and pressure", "Gravity and magnetic",
             "Magnetic and inertia", "Inertia and Gravity"),
    Question("Where does the light on the moon come from?", "Earth", "The moon gives off its own light", "Space",
             "Sun"),
    Question("What object do the planets of our solar system orbit around", "Earth", "The Moon", "Jupiter", "The Sun"),
    Question("Most places on Earth experience: ", "Snow", "Twisters", "Earthquakes", "Four seasons"),
    Question("Usually meteors ____________ the Earth’s atmosphere.", "Get bigger", "Get colder", "Bounce off",
             "Burn up in"),
    Question("Earth is the __________ planet from the sun.", "12", "100", "1,000", "Third"),
    Question("Meteors that land on earth are called___", "Satellites", "Kryptonites", "Metotites", "Meteorites"),
    Question("The Earth is shaped as a?", "Plane(Flat)", "Cube(Square)", "Pyramid(Triangle)", "Sphere(Circle)"),
    Question("What turns water on the Earth into vapor in the water cycle?", "The moon", "Global Warming",
             "Water treatment centers", "The sun"),
    Question("Studying the water cycle, where is the purest water on Earth?", "Rivers and streams", "Sulfur springs",
             "Lakes and ponds", "Glaciers and ice caps"),
    Question("Which object orbits the Earth?", "Sun", "Both the moon and sun", "Asteroids", "Moon"),
    Question("How long does it take the Earth to orbit the Sun?", "1 Day", "1 month", "Every Season", "1 Year"),
    Question("About how long does it take for the moon to orbit the Earth?", "1 Day", "1 year", "10 years", "1 month"),
    Question("What is a scientist called that studies space, but stays on earth?", "Meteorologist", "Astronaut",
             "Biologist", "Astronomer"),
    # Question("How long does it take for earth to rotate once?", "12 hours", "One week", "One month", "A Day"),
    Question("Rock and red dust made of__________ covers the surface of Mars.", "Nickel", "Clay", "Magnesium", "Iron"),
    Question("What do scientists believe lies beneath Mars’ surface?", "Gold", "Water", "Microscopic life", "Ice"),
    Question("How many moons does Mars have?", "1", "3", "4", "2"),
    Question("Mars is about __________ size of Earth.", "The same", "Twice the", "One and a half times the",
             "Half the"),
    Question("How is the temperature on Mars?", "Warm", "cool", "Hot", "Cold"),
    Question("Scientists believe Mars once had lots of _______________ . ", "Life", "Plants", "Oxygen", "Water"),
    Question("What does Mars have? ", "A Roller coasters", "Disney world", "Movie Theater",
             "Huge Volcanoes and craters"),
    Question("What is Mars sometimes called? ", "Earth 2", "Meatball", "Dr.Pepper", "The Red Planet"),
    Question("Oxygen, helium, and propane are examples of a", "Solid", "Liquid", "Mineral", "Gas"),
    Question("Matter is basically a solid, liquid, or gas that takes up", "Time", "Energy", "Heat", "Space"),
    Question("What is easier to see at night than in the day time", "The Sun", "Birds", "Clouds", "Stars"),

    Question("What is the sun?", "A Fast Food Place", "Something I could buy", "Another name for the moon", "A star"),
    Question("It takes __________ for the sun’s light to reach the earth.", "A cool 2 minutes", "Over 9,000 Days",
             "30 minutes", "8 minutes"),
    Question("What does the sun control?", "The color of my shoes", "Video Game prices", "The waves", "Seasons"),
    Question("The sun is made of ______ gases. ", "Farting", "Helium and neon", "Neon", "Hydrogen and Helium"),
    Question("What is the sun?", "Planet", "Giant planet", "Asteroid", "Star"),
    Question("Which celestial body has the most gravitational pull?", "Earth", "Moon", "Asteroid", "Sun"),
    Question("What two forces keep Earth in orbit with the sun?", "Heat and pressure", "Gravity and magnetic",
             "Magnetic and inertia", "Inertia and Gravity"),
    Question("Where does the light on the moon come from?", "Earth", "The moon gives off its own light", "Space",
             "Sun"),
    Question("What object do the planets of our solar system orbit around", "Earth", "The Moon", "Jupiter", "The Sun"),
    Question("The temperature of the sun is around _________ degrees Fahrenheit.", "10", "100", "1,000", "10,000"),
    Question("Why does the sun have a strong gravitational pull? ", "Color", "Smell", "Because NASA says it does",
             "Size"),
    Question("The sun makes up 98 percent of __________ in the solar system. ", "The Cotten Candy", "The Legos",
             "Pancake Batter", "Matter"),
]

mercury = Planet( questions[0], questions[1], questions[2], questions[3],questions[4], questions[5],questions[6], questions[7],questions[8], questions[9])
venus = Planet( questions[10], questions[11], questions[12], questions[13], questions[14], questions[15], questions[16], questions[17], questions[18], questions[19])
earth = Planet( questions[20], questions[21], questions[22], questions[23], questions[24], questions[25], questions[26], questions[27], questions[28], questions[29])
mars = Planet( questions[30], questions[31], questions[32], questions[33], questions[34], questions[35], questions[36],  questions[37], questions[38], questions[39])
#jupiter = Planet( questions[40], questions[41], questions[42], questions[43], questions[44], questions[45], questions[46],  questions[47], questions[48], questions[49])
#saturn = Planet( questions[50], questions[51], questions[52], questions[53], questions[54], questions[55], questions[56],  questions[57], questions[58], questions[59])
#uranus = Planet( questions[60], questions[61], questions[62], questions[63], questions[64], questions[65], questions[66],  questions[67], questions[68], questions[69])
#neptune = Planet( questions[70], questions[71], questions[72], questions[73], questions[74], questions[75], questions[76],  questions[77], questions[78], questions[79])

y = 0
x = 0
mercury.displayAllQuestions("Mercury", "Venus")
venus.displayAllQuestions("Venus", "Earth")
earth.displayAllQuestions("Earth", "Mars")
mars.displayAllQuestions("Mars", "Jupiter")
#jupiter.displayAllQuestions("Jupiter", "Saturn")
#saturn.displayAllQuestions("Saturn", "Uranus")
#uranus.displayAllQuestions("Uranus", "Neptune")
#neptune.displayAllQuestions("Neptune", "")
