"""
All narrative text for Calamari Union.
Organized by scene ID. Each scene has description blocks and choice text.
Tone: deadpan, dry, minimal. Very Kaurismaki.
English (SCENES), Finnish literal translation (SCENES_FI),
Finnish free version (SCENES_FI2) written fresh in Kaurismaki style.
"""

SCENES = {
    "intro": {
        "texts": [
            "Helsinki. Late at night. Or early in the morning. "
            "It makes no difference in Kallio.",
            "Fourteen men named Frank have gathered in a bar. "
            "They share a name, a cigarette brand, and a conviction "
            "that life must be better somewhere else.",
            "That somewhere is Eira. The seaside. The promised land. "
            "Or at least a neighborhood with better restaurants.",
            "A fifteenth man, Pekka, has joined them. "
            "He is not named Frank. He speaks English. "
            "Nobody asks why.",
            "Tonight, they move. Through alleys, tunnels, and the "
            "endless dark of a Finnish night. Most will not make it. "
            "Some will die. Some will simply... stop.",
            "You are Frank.",
        ],
        "choices": [
            "Begin the journey",
        ],
    },

    "ch01_bar": {
        "texts": [
            "The bar has no name. Or it has a name, but nobody remembers it. "
            "The ceiling is low. The smoke is thick. The beer is warm.",
            "Around a table, several Franks sit in silence. They have been "
            "sitting here for what might be hours or years. A man named Pekka "
            "is reading an English newspaper upside down.",
            "One of the Franks speaks: \"Eira.\" Another nods. "
            "A third lights a cigarette from the one he just finished. "
            "The plan, such as it is, has been made.",
        ],
        "choices": [
            "Leave through the front door",
            "Slip out the back",
            "Stay for one more drink",
            "Ask Pekka for advice",
        ],
        "extras": {
            "pekka_advice": "Pekka looks up from his newspaper. \"The shortest distance "
                "between two points,\" he says in English, \"is not always "
                "a straight line. Sometimes it is a drink. But not tonight.\"",
            "pekka_choice": "Leave through the front door",
        },
    },

    "ch02_alley": {
        "texts": [
            "The alley smells of rain and concrete. Apartment blocks rise "
            "on both sides like canyon walls. A cat watches from a window ledge "
            "with the indifference of a bureaucrat.",
            "Behind a row of garbage bins, a man in a dark coat is crouching. "
            "He looks up. He is, of course, also named Frank.",
            "\"Police,\" he says. \"Everywhere. Like cockroaches, but with badges.\"",
        ],
        "choices": [
            "Head toward the main road",
            "Cut through the courtyard",
            "Go back to the bar",
        ],
    },

    "ch02_dumpster": {
        "texts": [
            "The back exit leads to an alley full of dumpsters. The smell is "
            "creative. Somewhere, a dog barks with the weariness of a philosopher.",
            "A Frank is here, elbow-deep in a dumpster. He pulls out a folded "
            "piece of paper and studies it with the intensity of a man examining "
            "a Caravaggio.",
            "\"A map,\" he says. \"I think. Could be a menu. "
            "The streets and the soups look the same in this light.\"",
        ],
        "choices": [
            "Take the map",
            "Leave him to his archaeology",
        ],
        "extras": {
            "map_taken": "Frank takes the map. It is damp and smells of coffee grounds. "
                "Some of the streets are labeled. Some are not. "
                "It is the most helpful thing that has happened all night.",
            "map_choice": "Continue toward Hameentie",
        },
    },

    "ch03_hameentie": {
        "texts": [
            "Hameentie. The boulevard stretches into darkness like a sentence "
            "that refuses to end. Tram tracks gleam under streetlights. "
            "No trams. There are never trams when you need them.",
            "A Frank is trying to open a car door with a coat hanger. "
            "The car is a Lada. The coat hanger is bent. "
            "Frank's face shows neither frustration nor hope.",
        ],
        "choices": [
            "Help him steal the car",
            "Walk along the tram tracks",
            "Cross toward Sornäinen metro",
        ],
    },

    "ch03_courtyard": {
        "texts": [
            "The courtyard is quiet in the way that only Finnish courtyards "
            "can be quiet. Laundry hangs on lines like surrendered flags. "
            "The moon, if it exists, is hiding.",
            "A window on the third floor has light. A woman appears in it. "
            "She leans out and says something. It might be \"hello\" or "
            "\"help\" or \"who are you and why are you in my courtyard.\"",
        ],
        "choices": [
            "Talk to her",
            "Climb the fire escape to the roof",
            "Hide and wait",
        ],
        "extras": {
            "frank_fence": "Frank waits in the shadows. Minutes pass. An hour. "
                "Then another Frank appears, climbing over the fence "
                "from the other side. He nods, as if this meeting was "
                "prearranged, which it wasn't.",
            "fence_choice": "Continue together toward the metro",
        },
    },

    "ch04_car": {
        "texts": [
            "The Lada starts on the fourth try. This is considered lucky. "
            "Frank drives. The other Frank navigates by pointing vaguely south.",
            "The streets are empty. Helsinki at night is a city that has "
            "forgotten it exists. The Lada's headlights illuminate nothing "
            "of consequence.",
            "Near Hakaniemi, the engine makes a sound like a confession "
            "and dies. The car rolls to a stop beside a shuttered kiosk.",
        ],
        "choices": [
            "Continue on foot through the market",
            "Try to fix the car",
        ],
    },

    "ch04_metro": {
        "texts": [
            "The metro station is a cathedral of fluorescent light and "
            "institutional tile. The escalator moves downward with the "
            "determination of geological erosion.",
            "On a bench, a Frank sits smoking. The no-smoking sign above "
            "him is either broken or irrelevant. He stares at the empty tracks "
            "like a man watching television.",
            "\"No trains,\" he says. \"Not for hours. Maybe not ever again. "
            "Hard to tell the difference.\" He pauses. \"There is one, though. "
            "Down at the far end. Maintenance. Just sitting there.\"",
        ],
        "choices": [
            "Wait for a train anyway",
            "Walk into the tunnel",
            "Walk toward the maintenance train",
            "Take the escalator back up",
        ],
        "extras": {
            "wait_text": "Frank waits. The bench is hard. The fluorescent lights "
                "hum a single note, endlessly. Time passes. No train comes. "
                "No train was ever going to come.",
            "wait_choice": "Walk into the tunnel",
        },
    },

    "ch05_tunnels": {
        "texts": [
            "The tunnel swallows light the way Helsinki swallows hope: "
            "completely, and without apology. Water drips from the ceiling "
            "in a rhythm that almost sounds intentional.",
            "Deeper in, a Frank materializes from the darkness. He has been "
            "down here for what he claims is three days. His watch stopped "
            "on Tuesday. Today might be Friday. Or February.",
            "\"I know the way,\" he says. His eyes suggest otherwise, "
            "but in the dark, all directions are equal.",
        ],
        "choices": [
            "Follow his directions",
            "Go your own way",
            "Turn back",
        ],
    },

    "ch06_market": {
        "texts": [
            "Hakaniemi market square. The stalls are shuttered and locked, "
            "their contents unknown and unknowable until morning. "
            "A drunk man sits on a crate, singing something that might "
            "be a tango or might be a prayer.",
            "From behind a market stall, a Frank emerges. With him is Pekka, "
            "who says something in English about \"the dialectics of "
            "geographical displacement.\" Nobody responds.",
            "Ahead, bridges lead south. The water beneath them is black "
            "and patient.",
        ],
        "choices": [
            "Cross the Long Bridge",
            "Go through Siltasaari",
            "Follow the singing drunk",
        ],
    },

    "ch07_park": {
        "texts": [
            "Kaisaniemi Park. The trees stand like old men who have "
            "forgotten why they came outside. Through the branches, "
            "if you listen carefully, you can hear the sea.",
            "Or maybe it's traffic. In Helsinki, the two sound the same.",
            "On a bench, a Frank sleeps. His coat is pulled up to his ears. "
            "His breathing is the most peaceful thing in the city.",
        ],
        "choices": [
            "Wake him and continue together",
            "Let him sleep, continue alone",
            "Rest on the bench too",
        ],
    },

    "ch08_kruununhaka": {
        "texts": [
            "Kruununhaka. The buildings here are taller, cleaner, older. "
            "They look down at Frank the way buildings look down at people "
            "who don't belong. Which is to say: they look down.",
            "The architecture speaks of money and history and the kind of "
            "confidence that comes from never having lived in Kallio.",
            "A police car slides down the street like a shark through "
            "shallow water. Its lights are off but its intent is obvious.",
        ],
        "choices": [
            "Duck into a doorway",
            "Act natural, keep walking",
            "Run",
        ],
        "extras": {
            "police_pass": "Frank walks. The police car passes. Its occupants are "
                "drinking coffee and arguing about football. They do not "
                "look at Frank. Frank does not look at them. "
                "Two ships in the night.",
            "police_choice": "Continue to Esplanadi",
        },
    },

    "ch09_esplanadi": {
        "texts": [
            "Esplanadi. The boulevard is wide and tree-lined and, for "
            "the first time tonight, Frank can smell the sea. It smells "
            "like salt and diesel and the possibility of being somewhere else.",
            "Two Franks are here, arguing. One points west. The other points "
            "south. They have been arguing, apparently, since Kallio. "
            "Neither has moved.",
            "\"Eira is south,\" says one. \"Eira is a state of mind,\" "
            "says the other. Both might be right.",
        ],
        "choices": [
            "Go south toward Kaivopuisto",
            "Go west toward Kamppi",
            "Follow the arguing Franks",
            "Take Bulevardi",
        ],
        "extras": {
            "follow_south": "The Franks stop arguing and walk south. "
                "Frank follows. The argument resumes, but quieter now, "
                "as if the sea is already calming them.",
            "follow_south_choice": "Continue south",
            "follow_west": "The Franks turn west. \"Shortcut,\" one says. "
                "The other nods. Frank follows. "
                "The shortcut leads to Kamppi bus station.",
            "follow_west_choice": "...",
        },
    },

    "ch10_kaivopuisto": {
        "texts": [
            "Kaivopuisto. The park opens to the sea like a held breath "
            "finally released. Stars are visible. Wind moves through "
            "the grass. It carries salt.",
            "A Frank stands at the shore, looking out at the water. "
            "His silhouette is the loneliest thing in Finland, which is "
            "saying something.",
            "Beyond the park, to the west: Eira. You can almost see it. "
            "Or you can see something, and you choose to believe it's Eira.",
        ],
        "choices": [
            "Walk along the shoreline toward Eira",
            "Sit with this Frank and talk",
            "Take the street route",
        ],
        "extras": {
            "talk_1": "Frank sits beside the other Frank. They don't speak. "
                "The sea speaks for them — or doesn't, because the sea "
                "is also Finnish.",
            "talk_2": "After a while, the other Frank stands, buttons his coat, "
                "and walks into the water. Not dramatically. "
                "Just... walks. As if he's going to work.",
            "talk_3": "Frank watches. Then he stands, turns west, and walks "
                "toward Eira. Because that's what Franks do. They walk.",
            "talk_choice": "Walk toward Eira",
        },
    },

    "eira": {
        "texts": [
            "Eira.",
            "The sky is changing. Not sunrise — not yet — but the darkness "
            "is thinning, the way silence thins before someone speaks. "
            "The buildings here are art nouveau, pale and elegant, like "
            "people who have never had to run from anything.",
            "The sea is right there. Waves touch the rocks with a gentleness "
            "that Helsinki does not usually permit.",
            "You made it. You are in Eira.",
            "It looks exactly like the rest of Helsinki, "
            "only with better lighting.",
            "But you are here. And being here is the point. "
            "Or maybe the journey was the point. "
            "Or maybe there is no point, and that's the most Finnish "
            "conclusion of all.",
        ],
    },

    "ch03_rooftop": {
        "texts": [
            "The fence gives way to a fire escape that was built during a period "
            "of architectural optimism. The ladder ends two floors short. "
            "Frank climbs anyway.",
            "From the rooftop, Kallio spreads in every direction like a problem "
            "without a solution. To the south, lights. To the north, more Kallio. "
            "The wind up here has opinions.",
            "Another building is close enough to reach, if Frank is willing "
            "to trust a gap of about two meters and a lifetime of poor decisions.",
        ],
        "choices": [
            "Climb down to the street",
            "Cross to the next building",
            "Jump to the alley below",
        ],
    },

    "ch04_metro_train": {
        "texts": [
            "At the far end of the platform, a maintenance train sits in the dark. "
            "It looks abandoned in the way that everything in the Helsinki metro "
            "looks abandoned: professionally.",
            "The door is open. The controls are simple. A Frank is already "
            "inside, sitting in the driver's seat, studying the dashboard "
            "with the confidence of a man who has never operated anything "
            "more complex than a bottle opener.",
            "\"I drove a forklift once,\" he says. \"Same principle.\" "
            "It is not the same principle.",
        ],
        "choices": [
            "Let him drive",
            "Take the controls yourself",
            "Get out and walk the tunnel instead",
        ],
        "extras": {
            "let_drive_1": "Frank sits in the passenger seat. The other Frank pushes "
                "a lever. The train groans, shudders, and begins to move "
                "with the reluctance of a civil servant on Monday morning.",
            "let_drive_2": "Tunnel walls slide past. Stations appear and disappear "
                "like opportunities. The Frank at the controls hums "
                "tunelessly. The train emerges into open air near the harbor.",
            "let_drive_choice": "Step off at the harbor",
        },
    },

    "ch05_cafe": {
        "texts": [
            "The cafe is open because cafes in Kallio are always open. "
            "The lights are the color of headaches. The coffee is the "
            "temperature of regret.",
            "Inside, four Franks sit at separate tables, each pretending "
            "the others don't exist. This requires concentration, "
            "because they all look identical.",
            "A fifth Frank arrives, shaking rain from his coat. He nods "
            "at nobody in particular. \"I have a car outside,\" he says. "
            "\"A limousine. Well. A long car. The distinction is philosophical.\"",
        ],
        "choices": [
            "Go with the Frank and his limousine",
            "Leave through the back toward the market",
            "Stay for another coffee",
        ],
    },

    "ch06_limo": {
        "texts": [
            "The car is long and black and has seen better decades. "
            "The interior smells of pine air freshener and existential crisis. "
            "Frank gets in the back. The other Frank drives.",
            "They pass through streets that Frank has never seen, which is "
            "strange because Helsinki is not a large city. The driver hums "
            "something. It might be a tango or an engine warning.",
            "\"Where to?\" the driver asks, two kilometers into the journey. "
            "Planning is not a Finnish strength.",
        ],
        "choices": [
            "\"South. Toward the cathedral.\"",
            "\"Just drop me in Kruununhaka\"",
            "\"Run the red light, I'm in a hurry\"",
        ],
    },

    "ch05_harbor": {
        "texts": [
            "Sörnäisten satama. The harbor smells of diesel and fish and "
            "the particular sadness of industrial infrastructure at night. "
            "Cranes stand against the sky like metal giraffes contemplating "
            "retirement.",
            "A Frank leans against a bollard, smoking. He has the look "
            "of a man who has been waiting for a ship that will never come, "
            "which in Helsinki is everyone.",
            "\"Ships go to Tallinn,\" he says. \"But Tallinn is not Eira.\" "
            "He pauses. \"Nothing is Eira. That's the whole problem.\"",
        ],
        "choices": [
            "Follow the waterfront south",
            "Cut inland to the cafe lights",
            "Try to board a cargo ship",
        ],
    },

    "ch07_katajanokka": {
        "texts": [
            "Katajanokka. The buildings here are red brick and diplomatic "
            "certainty. Embassies sleep behind iron gates. Even the streetlights "
            "look classified.",
            "A Frank stands outside the Icebreaker Museum, reading a plaque "
            "he cannot see in the dark. \"Did you know,\" he says, \"that "
            "icebreakers work by riding up onto the ice and crushing it "
            "with their weight?\" He pauses. \"Like landlords.\"",
            "To the south, the silhouette of Uspenski Cathedral blocks out "
            "stars. Beyond it, somewhere, Esplanadi.",
        ],
        "choices": [
            "Continue south toward Esplanadi",
            "Walk toward the cathedral square",
            "Head to the ferry terminal",
        ],
    },

    "ch08_senate_square": {
        "texts": [
            "Senate Square. The cathedral looms white and enormous, "
            "like a wedding cake for a marriage between God and Finland. "
            "The steps are wide enough for an army. Tonight, they hold "
            "only pigeons and silence.",
            "At the bottom of the steps, a statue of Alexander II regards "
            "the empty square with the expression of a man who has been "
            "standing in one place for 130 years and is beginning to have "
            "regrets.",
            "From here, the streets slope south. Toward the sea. "
            "Toward Esplanadi. Toward something that might be Eira, "
            "if you believe in it hard enough.",
        ],
        "choices": [
            "Cross the square south toward Esplanadi",
            "Walk east toward Katajanokka",
            "Sit on the cathedral steps and rest",
        ],
    },

    "ch09_bulevardi": {
        "texts": [
            "Bulevardi. The name sounds French but the street is Finnish: "
            "long, dark, and going somewhere it hasn't told you about. "
            "Old apartment buildings line both sides with the dignity of "
            "pensioners who once owned things.",
            "At a corner, an all-night kiosk glows like a lighthouse for "
            "the lost. A man buys a sausage. Another man watches him buy "
            "the sausage. This is Helsinki nightlife.",
            "A Frank is here, leaning against a lamppost, studying a "
            "crumpled bus schedule as if it contains prophecy. \"Eira "
            "is that way,\" he says, pointing into the darkness. "
            "\"Two blocks. Maybe three. Distance is subjective after midnight.\"",
        ],
        "choices": [
            "Keep walking toward Eira",
            "Stop at the kiosk",
            "Cut through the park to Kaivopuisto",
        ],
    },

    # Death texts
    "death_bar_raid": {
        "texts": [
            "One more drink becomes two. Two becomes silence. "
            "The police arrive before the third.",
            "Frank's journey ended at the bar where it began. "
            "There is a certain symmetry in that. "
            "The police do not appreciate symmetry.",
        ],
    },
    "death_bar_return": {
        "texts": [
            "The bar is full of police. They are drinking the warm beer "
            "and examining Franks with the thoroughness of entomologists.",
            "Going back was never an option. "
            "Frank should have known this. Frank did know this.",
        ],
    },
    "death_car_fix": {
        "texts": [
            "Frank opens the hood. The engine looks back at him "
            "with the complexity of a philosophical argument.",
            "The police car arrives before Frank can formulate a response. "
            "The Lada, at least, dies with its hood up.",
        ],
    },
    "death_tunnel_train": {
        "texts": [
            "Frank chooses his own path. In the dark, all paths feel valid. "
            "This one leads into the path of a maintenance train.",
            "The driver never sees Frank. Frank never sees the driver. "
            "Two strangers passing in the night, briefly.",
        ],
    },
    "death_police_stop": {
        "texts": [
            "\"Act natural\" is advice that only works for people who know "
            "what natural looks like. Frank, walking through Kruununhaka "
            "at 3 AM in a long coat, does not look natural.",
            "The police are polite. This makes it worse.",
        ],
    },
    "death_police_run": {
        "texts": [
            "Frank runs. The police give chase. Frank is fast but the night "
            "is faster, and the pavement catches his foot with the precision "
            "of a Finnish winter.",
            "Running from the police in Kruununhaka. "
            "It's the most exercise this neighborhood has seen in years.",
        ],
    },
    "death_street_patrol": {
        "texts": [
            "The street route passes directly through a police checkpoint. "
            "They have been waiting all night for someone exactly like Frank.",
            "So close to Eira. Close enough to smell the sea. "
            "But the sea smells the same from a police van.",
        ],
    },
    "death_tram_tracks": {
        "texts": [
            "Frank walks along the tram tracks. The rails hum beneath his feet "
            "with a frequency that feels almost companionable. No trams, he thinks. "
            "There are never trams.",
            "There is a tram.",
            "The driver, who has been operating the night maintenance route for "
            "eleven years, later describes Frank as \"a man who looked surprised "
            "by the concept of public transportation.\"",
        ],
    },

    "death_rooftop_fall": {
        "texts": [
            "Frank jumps. For a moment, he is the freest man in Kallio. "
            "Gravity, however, is not interested in freedom. "
            "Gravity is interested in physics.",
            "The alley receives him with the hospitality of concrete. "
            "Three floors is not a long fall, but it is long enough.",
        ],
    },
    "death_metro_crash": {
        "texts": [
            "Frank pushes the lever forward. The train responds with "
            "enthusiasm. The tunnel wall responds with finality.",
            "The Helsinki metro system will later report a minor maintenance "
            "incident. Frank, who has become part of the infrastructure, "
            "is not available for comment.",
        ],
    },
    "death_limo_police": {
        "texts": [
            "The light is red. The driver runs it. A police car, which has "
            "been sitting at the intersection with the patience of a Finnish "
            "winter, follows.",
            "Two Franks in a stolen limousine running a red light at 3 AM. "
            "The police report writes itself. The judge will not need long.",
        ],
    },
    "death_coast_guard": {
        "texts": [
            "Frank climbs the gangway of a cargo ship. He makes it three "
            "steps before a flashlight finds him. The coast guard officer "
            "looks tired. Frank looks caught.",
            "The ship was going to Lübeck. Frank is going to a holding cell. "
            "Lübeck is not Eira, but neither is a cell. At least the cell "
            "is warm.",
        ],
    },
    "death_senate_patrol": {
        "texts": [
            "Frank sits on the cathedral steps. The stone is cold. "
            "His eyes close for just a moment.",
            "The patrol car finds him at 4 AM, sleeping against a column "
            "like a saint who has given up on miracles. The officers are "
            "gentle. The handcuffs are not.",
        ],
    },

    # Lost endings
    "lost_woman": {
        "texts": [
            "She makes coffee. The apartment is warm. There is a cat. "
            "The cat does not care about Eira.",
            "Frank sits down. He never gets up. The coffee is replaced by "
            "dinner, dinner by breakfast, breakfast by years.",
            "Frank never reached Eira. But perhaps Eira was never "
            "meant to be reached. Perhaps it was always a kitchen, "
            "a cat, and coffee that someone else made.",
        ],
    },
    "lost_drunk": {
        "texts": [
            "The drunk's song is a tango. Frank knows the words. "
            "He shouldn't, but he does. They sing together. "
            "The song has forty verses.",
            "Somewhere around verse thirty-seven, Frank forgets about Eira. "
            "By verse forty, he forgets about everything.",
            "He wakes in Kallio. It is morning. The journey is over "
            "before the destination. The tango continues.",
        ],
    },
    "lost_bench": {
        "texts": [
            "The bench is comfortable in the way that exhaustion makes "
            "anything comfortable. Frank closes his eyes for one moment.",
            "Morning finds him still there. The park is full of joggers "
            "and dog walkers and people who reached their destinations "
            "hours ago.",
            "Frank never reached Eira. He reached a bench. "
            "Some journeys end where tiredness decides.",
        ],
    },
    "lost_kamppi": {
        "texts": [
            "West. Kamppi. The bus station. A place people leave from, "
            "not arrive at. Frank has confused his directions.",
            "He boards a bus. It goes to Espoo. Espoo is not Eira. "
            "Espoo is not anything, really.",
            "Frank never reached Eira. He reached the suburbs. "
            "This is the saddest ending of all.",
        ],
    },
    "lost_cafe": {
        "texts": [
            "Frank orders another coffee. The waitress, who has seen this "
            "before, says nothing. The coffee comes. It is identical to "
            "the last one.",
            "Hours pass. The other Franks leave, one by one, toward "
            "destinations they may or may not reach. Frank stays. "
            "The coffee stays.",
            "He is still there in the morning, when the day shift arrives "
            "and the night becomes a story that nobody tells. Eira is south. "
            "The cafe is here. Some distances cannot be crossed with caffeine.",
        ],
    },
    "lost_ferry": {
        "texts": [
            "The ferry terminal is bright and warm and full of people going "
            "to Stockholm. Stockholm is not Eira. Stockholm is not even "
            "Helsinki. But the ferry is leaving in twenty minutes and Frank "
            "is tired of walking.",
            "He boards. The Baltic Sea is black and vast and indifferent. "
            "Frank stands at the rail and watches Helsinki shrink.",
            "He never reached Eira. He reached the duty-free shop. "
            "The vodka is cheaper here, which is the most Finnish "
            "consolation available.",
        ],
    },
    "lost_kiosk": {
        "texts": [
            "Frank orders a sausage. It comes in a bun with mustard. "
            "He eats it standing, in the Finnish tradition of consuming "
            "food without acknowledging pleasure.",
            "He orders another. And another. The kiosk man, who has worked "
            "nights for seventeen years, recognizes the look. It is the look "
            "of a man who has stopped walking.",
            "Frank never reached Eira. He reached a kiosk. Eira is two "
            "blocks south, but two blocks is infinity when your feet have "
            "decided to negotiate.",
        ],
    },
}


# --- Finnish translation ---

SCENES_FI = {
    "intro": {
        "texts": [
            "Helsinki. Myöhään yöllä. Tai aikaisin aamulla. "
            "Kalliossa sillä ei ole väliä.",
            "Neljätoista miestä nimeltä Frank on kokoontunut baariin. "
            "Heillä on yhteinen nimi, tupakkamerkki ja vakaumus, "
            "että elämän täytyy olla parempaa jossain muualla.",
            "Se jossain on Eira. Merenranta. Luvattu maa. "
            "Tai ainakin kaupunginosa, jossa on paremmat ravintolat.",
            "Viidestoista mies, Pekka, on liittynyt heihin. "
            "Hänen nimensä ei ole Frank. Hän puhuu englantia. "
            "Kukaan ei kysy miksi.",
            "Tänä yönä he liikkuvat. Kujien, tunnelien ja "
            "suomalaisen yön loputtoman pimeyden läpi. Useimmat eivät pääse perille. "
            "Jotkut kuolevat. Jotkut yksinkertaisesti... pysähtyvät.",
            "Sinä olet Frank.",
        ],
        "choices": [
            "Aloita matka",
        ],
    },

    "ch01_bar": {
        "texts": [
            "Baarilla ei ole nimeä. Tai on, mutta kukaan ei muista sitä. "
            "Katto on matala. Savu on paksua. Olut on lämmintä.",
            "Pöydän ympärillä istuu useita Frankeja hiljaisuudessa. He ovat "
            "istuneet siinä tunteja tai vuosia. Pekka-niminen mies "
            "lukee englanninkielistä sanomalehteä ylösalaisin.",
            "Yksi Frankeista puhuu: \"Eira.\" Toinen nyökkää. "
            "Kolmas sytyttää tupakan edellisestä. "
            "Suunnitelma, sellainen kuin se on, on tehty.",
        ],
        "choices": [
            "Poistu etuovesta",
            "Lähde takaoven kautta",
            "Jää vielä yhdelle",
            "Kysy Pekalta neuvoa",
        ],
        "extras": {
            "pekka_advice": "Pekka nostaa katseensa lehdestä. \"Lyhin etäisyys "
                "kahden pisteen välillä\", hän sanoo englanniksi, \"ei ole aina "
                "suora viiva. Joskus se on juoma. Mutta ei tänä yönä.\"",
            "pekka_choice": "Poistu etuovesta",
        },
    },

    "ch02_alley": {
        "texts": [
            "Kuja tuoksuu sateelta ja betonilta. Kerrostalot kohoavat "
            "molemmin puolin kuin kanjonin seinät. Kissa katselee ikkunalaudalta "
            "virkamiehen välinpitämättömyydellä.",
            "Roskisten takana kyyhöttää mies tummassa takissa. "
            "Hän nostaa katseensa. Hänen nimensä on tietysti Frank.",
            "\"Poliiseja\", hän sanoo. \"Kaikkialla. Kuin torakoita, mutta virkamerkillä.\"",
        ],
        "choices": [
            "Suuntaa pääkadulle",
            "Oikaise sisäpihan kautta",
            "Palaa baariin",
        ],
    },

    "ch02_dumpster": {
        "texts": [
            "Takaovi johtaa kujalle täynnä jäteastioita. Haju on "
            "luova. Jossain koira haukkuu filosofin väsymyksellä.",
            "Täällä on Frank, kyynärpäitä myöten jäteastiassa. Hän vetää esiin "
            "taitetun paperin ja tutkii sitä sillä intensiteetillä, jolla mies "
            "tutkisi Caravaggiota.",
            "\"Kartta\", hän sanoo. \"Luulen. Voi olla ruokalista. "
            "Kadut ja keitot näyttävät samalta tässä valossa.\"",
        ],
        "choices": [
            "Ota kartta",
            "Jätä hänet arkeologiansa pariin",
        ],
        "extras": {
            "map_taken": "Frank ottaa kartan. Se on kostea ja tuoksuu kahvinporoilta. "
                "Joihinkin katuihin on merkitty nimet. Joihinkin ei. "
                "Se on hyödyllisin asia, mitä koko yönä on tapahtunut.",
            "map_choice": "Jatka kohti Hämeentietä",
        },
    },

    "ch03_hameentie": {
        "texts": [
            "Hämeentie. Bulevardi ulottuu pimeyteen kuin lause, "
            "joka kieltäytyy loppumasta. Raitiovaunukiskot kiiltävät "
            "katulamppujen alla. Ei ratikoita. Ratikoita ei ole koskaan kun niitä tarvitsee.",
            "Frank yrittää avata auton ovea henkarilla. "
            "Auto on Lada. Henkari on vääntynyt. "
            "Frankin kasvot eivät ilmaise turhautumista eivätkä toivoa.",
        ],
        "choices": [
            "Auta häntä varastamaan auto",
            "Kävele ratikkakiskoja pitkin",
            "Suuntaa Sörnäisten metroon",
        ],
    },

    "ch03_courtyard": {
        "texts": [
            "Sisäpiha on hiljainen sillä tavalla, jolla vain suomalaiset "
            "sisäpihat voivat olla hiljaisia. Pyykit roikkuvat naruilla "
            "kuin antautumisliput. Kuu, jos se on olemassa, piilottelee.",
            "Kolmannen kerroksen ikkunassa on valoa. Nainen ilmestyy siihen. "
            "Hän kumartuu ulos ja sanoo jotain. Se voi olla \"hei\" tai "
            "\"apua\" tai \"kuka sinä olet ja miksi olet sisäpihallani.\"",
        ],
        "choices": [
            "Puhu hänelle",
            "Kiipeä palotikkaita katolle",
            "Piiloudu ja odota",
        ],
        "extras": {
            "frank_fence": "Frank odottaa varjoissa. Minuutteja kuluu. Tunti. "
                "Sitten toinen Frank ilmestyy, kiipeää aidan yli "
                "toiselta puolelta. Hän nyökkää, ikään kuin tapaaminen olisi "
                "sovittu ennalta, mitä se ei ollut.",
            "fence_choice": "Jatka yhdessä metroa kohti",
        },
    },

    "ch04_car": {
        "texts": [
            "Lada käynnistyy neljännellä yrityksellä. Tätä pidetään onnekkaana. "
            "Frank ajaa. Toinen Frank navigoi osoittamalla epämääräisesti etelään.",
            "Kadut ovat tyhjiä. Helsinki yöllä on kaupunki, joka on "
            "unohtanut olevansa olemassa. Ladan ajovalot valaisevat "
            "ei mitään merkittävää.",
            "Hakaniemen lähellä moottori päästää äänen kuin tunnustuksen "
            "ja kuolee. Auto rullaa pysähdyksiin suljetun kioskin viereen.",
        ],
        "choices": [
            "Jatka jalan torin kautta",
            "Yritä korjata autoa",
        ],
    },

    "ch04_metro": {
        "texts": [
            "Metroasema on loisteputkivalon ja virastolaatan katedraali. "
            "Liukuportaat laskeutuvat geologisen eroosion päättäväisyydellä.",
            "Penkillä istuu Frank ja polttaa tupakkaa. Tupakointi kielletty "
            "-kyltti hänen yläpuolellaan on joko rikki tai epäolennainen. "
            "Hän tuijottaa tyhjille raiteille kuin televisio-ohjelmaa katsova mies.",
            "\"Ei junia\", hän sanoo. \"Ei tunteihin. Ehkä ei enää koskaan. "
            "Vaikea erottaa.\" Hän pitää tauon. \"Yksi tosin on. "
            "Tuolla perällä. Huoltojuna. Seisoo vain siinä.\"",
        ],
        "choices": [
            "Odota junaa joka tapauksessa",
            "Kävele tunneliin",
            "Kävele huoltojunan luo",
            "Nouse liukuportaita takaisin ylös",
        ],
        "extras": {
            "wait_text": "Frank odottaa. Penkki on kova. Loisteputket "
                "hurisevat yhtä ainoaa säveltä loputtomiin. Aika kuluu. Juna ei tule. "
                "Juna ei ollut koskaan tulossa.",
            "wait_choice": "Kävele tunneliin",
        },
    },

    "ch05_tunnels": {
        "texts": [
            "Tunneli nielee valon samalla tavalla kuin Helsinki nielee toivon: "
            "täydellisesti ja anteeksipyytelemättä. Vesi tippuu katosta "
            "rytmillä, joka kuulostaa melkein tarkoitukselliselta.",
            "Syvemmällä Frank materialisoituu pimeydestä. Hän on ollut "
            "täällä omien sanojensa mukaan kolme päivää. Hänen kellonsa pysähtyi "
            "tiistaina. Tänään voi olla perjantai. Tai helmikuu.",
            "\"Tiedän tien\", hän sanoo. Hänen silmänsä viittaavat toisin, "
            "mutta pimeässä kaikki suunnat ovat samanarvoisia.",
        ],
        "choices": [
            "Seuraa hänen ohjeitaan",
            "Mene omaa tietä",
            "Käänny takaisin",
        ],
    },

    "ch06_market": {
        "texts": [
            "Hakaniemen tori. Kojut ovat suljettuja ja lukittuja, "
            "niiden sisältö tuntematon ja arvaamaton aamuun asti. "
            "Humalainen mies istuu laatikolla ja laulaa jotain, joka voi olla "
            "tango tai rukous.",
            "Kojun takaa ilmestyy Frank. Hänen kanssaan on Pekka, "
            "joka sanoo jotain englanniksi \"maantieteellisen "
            "siirtymän dialektiikasta\". Kukaan ei vastaa.",
            "Edessä sillat johtavat etelään. Vesi niiden alla on mustaa "
            "ja kärsivällistä.",
        ],
        "choices": [
            "Ylitä Pitkäsilta",
            "Kulje Siltasaaren kautta",
            "Seuraa laulavaa juoppoa",
        ],
    },

    "ch07_park": {
        "texts": [
            "Kaisaniemen puisto. Puut seisovat kuin vanhat miehet, jotka ovat "
            "unohtaneet miksi he tulivat ulos. Oksien läpi, "
            "jos kuuntelee tarkasti, voi kuulla meren.",
            "Tai ehkä se on liikennettä. Helsingissä ne kuulostavat samalta.",
            "Penkillä Frank nukkuu. Hänen takkinsa on vedetty korviin asti. "
            "Hänen hengityksensä on kaupungin rauhallisinta.",
        ],
        "choices": [
            "Herätä hänet ja jatka yhdessä",
            "Anna hänen nukkua, jatka yksin",
            "Lepää penkillä sinäkin",
        ],
    },

    "ch08_kruununhaka": {
        "texts": [
            "Kruununhaka. Täällä rakennukset ovat korkeampia, siistimpiä, vanhempia. "
            "Ne katsovat Frankia alaspäin, kuten rakennukset katsovat ihmisiä, "
            "jotka eivät kuulu joukkoon. Eli: ne katsovat alaspäin.",
            "Arkkitehtuuri puhuu rahasta ja historiasta ja siitä itsevarmuudesta, "
            "joka tulee siitä, ettei ole koskaan asunut Kalliossa.",
            "Poliisiauto liukuu kadulla kuin hai matalassa vedessä. "
            "Sen valot ovat pois päältä, mutta tarkoitus on ilmeinen.",
        ],
        "choices": [
            "Väistä oviaukkoon",
            "Käyttäydy luonnollisesti, jatka kävelyä",
            "Juokse",
        ],
        "extras": {
            "police_pass": "Frank kävelee. Poliisiauto ohittaa. Sen miehistö "
                "juo kahvia ja kiistelee jalkapallosta. He eivät katso "
                "Frankia. Frank ei katso heitä. "
                "Kaksi laivaa yössä.",
            "police_choice": "Jatka Esplanadille",
        },
    },

    "ch09_esplanadi": {
        "texts": [
            "Esplanadi. Bulevardi on leveä ja puiden reunustama, ja "
            "ensimmäistä kertaa tänä yönä Frank voi haistaa meren. Se tuoksuu "
            "suolalta ja dieseliltä ja mahdollisuudelta olla jossain muualla.",
            "Kaksi Frankia on täällä, riitelemässä. Toinen osoittaa länteen. "
            "Toinen osoittaa etelään. He ovat riidelleet ilmeisesti "
            "Kalliosta asti. Kumpikaan ei ole liikkunut.",
            "\"Eira on etelässä\", sanoo toinen. \"Eira on mielentila\", "
            "sanoo toinen. Molemmat voivat olla oikeassa.",
        ],
        "choices": [
            "Mene etelään kohti Kaivopuistoa",
            "Mene länteen kohti Kamppia",
            "Seuraa riiteleviä Frankeja",
            "Ota Bulevardi",
        ],
        "extras": {
            "follow_south": "Frankit lopettavat riitelyn ja kävelevät etelään. "
                "Frank seuraa. Riita jatkuu, mutta hiljaisempana, "
                "ikään kuin meri jo rauhoittaisi heitä.",
            "follow_south_choice": "Jatka etelään",
            "follow_west": "Frankit kääntyvät länteen. \"Oikotie\", sanoo toinen. "
                "Toinen nyökkää. Frank seuraa. "
                "Oikotie johtaa Kampin linja-autoasemalle.",
            "follow_west_choice": "...",
        },
    },

    "ch10_kaivopuisto": {
        "texts": [
            "Kaivopuisto. Puisto avautuu merelle kuin pidätetty hengitys "
            "vihdoin vapautettuna. Tähdet näkyvät. Tuuli liikkuu "
            "ruohossa. Se kantaa suolaa.",
            "Frank seisoo rannalla ja katsoo vettä. "
            "Hänen siluettinsa on Suomen yksinäisin asia, mikä on "
            "paljon sanottu.",
            "Puiston takana, lännessä: Eira. Sen melkein näkee. "
            "Tai näkee jotain, ja päättää uskoa, että se on Eira.",
        ],
        "choices": [
            "Kävele rantaviivaa pitkin kohti Eiraa",
            "Istu tämän Frankin kanssa ja juttele",
            "Kulje katua pitkin",
        ],
        "extras": {
            "talk_1": "Frank istuu toisen Frankin viereen. He eivät puhu. "
                "Meri puhuu heidän puolestaan — tai ei puhu, koska meri "
                "on myös suomalainen.",
            "talk_2": "Hetken kuluttua toinen Frank nousee, napittaa takkinsa "
                "ja kävelee veteen. Ei dramaattisesti. "
                "Vain... kävelee. Kuin menisi töihin.",
            "talk_3": "Frank katsoo. Sitten hän nousee, kääntyy länteen ja kävelee "
                "kohti Eiraa. Koska sitä Frankit tekevät. He kävelevät.",
            "talk_choice": "Kävele kohti Eiraa",
        },
    },

    "eira": {
        "texts": [
            "Eira.",
            "Taivas muuttuu. Ei auringonnousu — ei vielä — mutta pimeys "
            "ohenee, kuten hiljaisuus ohenee ennen kuin joku puhuu. "
            "Rakennukset ovat jugend-tyylisiä, vaaleita ja elegantteja, kuin "
            "ihmisiä, joiden ei ole koskaan tarvinnut juosta pakoon.",
            "Meri on aivan siinä. Aallot koskettavat kiviä lempeydellä, "
            "jota Helsinki ei yleensä salli.",
            "Pääsit perille. Olet Eirassa.",
            "Se näyttää täsmälleen samalta kuin muu Helsinki, "
            "mutta paremmalla valaistuksella.",
            "Mutta olet täällä. Ja täällä oleminen on tarkoitus. "
            "Tai ehkä matka oli tarkoitus. "
            "Tai ehkä tarkoitusta ei ole, ja se on kaikkein suomalaisin "
            "johtopäätös.",
        ],
    },

    "ch03_rooftop": {
        "texts": [
            "Aita johtaa palotikkaille, jotka rakennettiin arkkitehtuurisen "
            "optimismin aikakaudella. Tikkaat loppuvat kaksi kerrosta liian aikaisin. "
            "Frank kiipeää silti.",
            "Katolta Kallio leviää joka suuntaan kuin ongelma "
            "ilman ratkaisua. Etelässä valoja. Pohjoisessa lisää Kalliota. "
            "Tuulella on täällä mielipiteitä.",
            "Toinen rakennus on tarpeeksi lähellä, jos Frank on valmis "
            "luottamaan noin kahden metrin rakoon ja elinikäisiin huonoihin päätöksiin.",
        ],
        "choices": [
            "Kiipeä alas kadulle",
            "Ylitä seuraavaan rakennukseen",
            "Hyppää kujalle",
        ],
    },

    "ch04_metro_train": {
        "texts": [
            "Laiturin perällä seisoo huoltojuna pimeässä. "
            "Se näyttää hylätyltä sillä tavalla, jolla kaikki Helsingin metrossa "
            "näyttää hylätyltä: ammattimaisesti.",
            "Ovi on auki. Ohjaimet ovat yksinkertaiset. Frank istuu jo "
            "kuljettajan paikalla ja tutkii kojelautaa "
            "sillä itsevarmuudella, joka on ominaista miehelle, joka ei ole koskaan "
            "käyttänyt mitään monimutkaisempaa kuin pullonavaaja.",
            "\"Ajoin kerran trukkia\", hän sanoo. \"Sama periaate.\" "
            "Se ei ole sama periaate.",
        ],
        "choices": [
            "Anna hänen ajaa",
            "Ota itse ohjaimet",
            "Poistu ja kävele tunnelissa",
        ],
        "extras": {
            "let_drive_1": "Frank istuu matkustajan paikalle. Toinen Frank työntää "
                "vipua. Juna vaikeroi, tärisee ja lähtee liikkeelle "
                "virkamiehen maanantaiaamun haluttomuudella.",
            "let_drive_2": "Tunnelin seinät liukuvat ohi. Asemat ilmestyvät ja katoavat "
                "kuin mahdollisuudet. Frank ohjaimissa hyräilee "
                "epävireisesti. Juna nousee ulkoilmaan sataman lähellä.",
            "let_drive_choice": "Nouse pois satamassa",
        },
    },

    "ch05_cafe": {
        "texts": [
            "Kahvila on auki, koska kahvilat Kalliossa ovat aina auki. "
            "Valot ovat päänsäryn värisiä. Kahvi on "
            "katumuksen lämpöistä.",
            "Sisällä neljä Frankia istuu eri pöydissä, kukin teeskennellen "
            "ettei muita ole olemassa. Tämä vaatii keskittymistä, "
            "koska he kaikki näyttävät identtisiltä.",
            "Viides Frank saapuu, ravistellen sadetta takistaan. Hän nyökkää "
            "ei kenellekään erityisesti. \"Minulla on auto ulkona\", hän sanoo. "
            "\"Limusiini. No. Pitkä auto. Ero on filosofinen.\"",
        ],
        "choices": [
            "Lähde Frankin ja hänen limusiininsa mukaan",
            "Poistu takakautta torille päin",
            "Jää toiselle kahville",
        ],
    },

    "ch06_limo": {
        "texts": [
            "Auto on pitkä ja musta ja on nähnyt parempia vuosikymmeniä. "
            "Sisätilat tuoksuvat mäntyilmanraikastimelta ja eksistentiaaliselta kriisiltä. "
            "Frank menee takapenkille. Toinen Frank ajaa.",
            "He ajavat katujen halki, joita Frank ei ole koskaan nähnyt, mikä on "
            "outoa, koska Helsinki ei ole suuri kaupunki. Kuljettaja hyräilee "
            "jotain. Se voi olla tango tai moottorin varoitusääni.",
            "\"Minne?\" kuljettaja kysyy, kaksi kilometriä matkan jälkeen. "
            "Suunnittelu ei ole suomalaisten vahvuus.",
        ],
        "choices": [
            "\"Etelään. Kohti tuomiokirkkoa.\"",
            "\"Jätä minut Kruununhakaan\"",
            "\"Aja päin punaista, minulla on kiire\"",
        ],
    },

    "ch05_harbor": {
        "texts": [
            "Sörnäisten satama. Satama tuoksuu dieseliltä ja kalalta ja "
            "siltä erityiseltä surullisuudelta, joka on ominaista teollisuusinfrastruktuurille "
            "yöaikaan. Nosturit seisovat taivasta vasten kuin metallikirahvit, "
            "jotka harkitsevat eläkkeelle jäämistä.",
            "Frank nojaa pollariin ja polttaa. Hänellä on sellaisen "
            "miehen ilme, joka on odottanut laivaa, joka ei koskaan tule, "
            "mikä Helsingissä tarkoittaa kaikkia.",
            "\"Laivat menevät Tallinnaan\", hän sanoo. \"Mutta Tallinna ei ole Eira.\" "
            "Hän pitää tauon. \"Mikään ei ole Eira. Siinä se ongelma.\"",
        ],
        "choices": [
            "Seuraa rantaviivaa etelään",
            "Oikaise sisämaahan kahvilan valoja kohti",
            "Yritä nousta rahtilaivaan",
        ],
    },

    "ch07_katajanokka": {
        "texts": [
            "Katajanokka. Rakennukset ovat punaista tiiltä ja diplomaattista "
            "varmuutta. Suurlähetystöt nukkuvat rautaporttien takana. Jopa "
            "katulamput näyttävät salaisiksi luokitelluilta.",
            "Frank seisoo Jäänmurtajamuseon edessä ja lukee kylttiä, "
            "jota hän ei näe pimeässä. \"Tiesitkö\", hän sanoo, \"että "
            "jäänmurtajat toimivat nousemalla jään päälle ja murskaamalla sen "
            "painollaan?\" Hän pitää tauon. \"Kuin vuokranantajat.\"",
            "Etelässä Uspenskin katedraalin siluetti peittää "
            "tähdet. Sen takana, jossain, Esplanadi.",
        ],
        "choices": [
            "Jatka etelään kohti Esplanadia",
            "Kävele tuomiokirkon aukiolle",
            "Suuntaa lauttaterminaaliin",
        ],
    },

    "ch08_senate_square": {
        "texts": [
            "Senaatintori. Tuomiokirkko kohoaa valkoisena ja valtavana "
            "kuin hääkakku Jumalan ja Suomen avioliitolle. "
            "Portaat ovat tarpeeksi leveät armeijalle. Tänä yönä niillä on "
            "vain kyyhkysiä ja hiljaisuutta.",
            "Portaiden juuressa Aleksanteri II:n patsas tarkastelee "
            "tyhjää toria sillä ilmeellä, joka tulee siitä, kun on "
            "seissyt samassa paikassa 130 vuotta ja alkaa "
            "katua.",
            "Täältä kadut viettävät etelään. Kohti merta. "
            "Kohti Esplanadia. Kohti jotain, joka voisi olla Eira, "
            "jos uskoo tarpeeksi kovasti.",
        ],
        "choices": [
            "Ylitä tori etelään kohti Esplanadia",
            "Kävele itään kohti Katajanokkaa",
            "Istu tuomiokirkon portaille ja lepää",
        ],
    },

    "ch09_bulevardi": {
        "texts": [
            "Bulevardi. Nimi kuulostaa ranskalaiselta, mutta katu on suomalainen: "
            "pitkä, pimeä ja menossa jonnekin, mistä se ei ole kertonut. "
            "Vanhat kerrostalot reunustavat molempia puolia eläkeläisten "
            "arvokkuudella.",
            "Kulmassa yökioski hehkuu kuin majakka "
            "eksyneille. Mies ostaa nakkia. Toinen mies katsoo, kun hän ostaa "
            "nakkia. Tämä on Helsingin yöelämää.",
            "Täällä on Frank, nojaamassa lyhtypylvääseen, tutkimassa "
            "rypistynyttä bussiaikataulua kuin se sisältäisi profetian. \"Eira "
            "on tuonne\", hän sanoo osoittaen pimeyteen. "
            "\"Kaksi korttelia. Ehkä kolme. Etäisyys on subjektiivista keskiyön jälkeen.\"",
        ],
        "choices": [
            "Jatka kävelyä kohti Eiraa",
            "Pysähdy kioskilla",
            "Oikaise puiston läpi Kaivopuistoon",
        ],
    },

    # Kuolemat
    "death_bar_raid": {
        "texts": [
            "Yhdestä juomasta tulee kaksi. Kahdesta tulee hiljaisuus. "
            "Poliisi saapuu ennen kolmatta.",
            "Frankin matka päättyi baariin, josta se alkoi. "
            "Siinä on tietty symmetria. "
            "Poliisi ei arvosta symmetriaa.",
        ],
    },
    "death_bar_return": {
        "texts": [
            "Baari on täynnä poliiseja. He juovat lämmintä olutta "
            "ja tutkivat Frankeja entomologin perusteellisuudella.",
            "Takaisin palaaminen ei ollut koskaan vaihtoehto. "
            "Frankin olisi pitänyt tietää tämä. Frank tiesi tämän.",
        ],
    },
    "death_car_fix": {
        "texts": [
            "Frank avaa konepellin. Moottori katsoo häntä takaisin "
            "filosofisen argumentin monimutkaisuudella.",
            "Poliisiauto saapuu ennen kuin Frank ehtii muotoilla vastausta. "
            "Lada ainakin kuolee konepelti auki.",
        ],
    },
    "death_tunnel_train": {
        "texts": [
            "Frank valitsee oman tiensä. Pimeässä kaikki tiet tuntuvat oikeilta. "
            "Tämä johtaa huoltojunan eteen.",
            "Kuljettaja ei näe Frankia. Frank ei näe kuljettajaa. "
            "Kaksi tuntematonta ohittaa toisensa yössä, hetkellisesti.",
        ],
    },
    "death_police_stop": {
        "texts": [
            "\"Käyttäydy luonnollisesti\" on neuvo, joka toimii vain niille, "
            "jotka tietävät miltä luonnollinen näyttää. Frank, kävelemässä "
            "Kruununhaan halki kello 3 yöllä pitkässä takissa, ei näytä luonnolliselta.",
            "Poliisit ovat kohteliaita. Tämä tekee asiasta pahemman.",
        ],
    },
    "death_police_run": {
        "texts": [
            "Frank juoksee. Poliisi jahtaa. Frank on nopea, mutta yö on "
            "nopeampi, ja jalkakäytävä nappaa hänen jalkansa suomalaisen "
            "talven tarkkuudella.",
            "Juoksemista poliisilta karkuun Kruununhaassa. "
            "Se on eniten liikuntaa, mitä tämä kaupunginosa on nähnyt vuosiin.",
        ],
    },
    "death_street_patrol": {
        "texts": [
            "Katu vie suoraan poliisin tiesulun läpi. "
            "He ovat odottaneet koko yön jotakuta juuri Frankin kaltaista.",
            "Niin lähellä Eiraa. Tarpeeksi lähellä haistaakseen meren. "
            "Mutta meri tuoksuu samalta poliisiautosta.",
        ],
    },
    "death_tram_tracks": {
        "texts": [
            "Frank kävelee ratikkakiskoja pitkin. Kiskot hurisevat hänen "
            "jalkojensa alla taajuudella, joka tuntuu melkein toverilliselta. "
            "Ei ratikoita, hän ajattelee. Ratikoita ei ole koskaan.",
            "On ratikka.",
            "Kuljettaja, joka on ajanut yöhuoltoreittiä yhdentoista vuoden ajan, "
            "kuvailee Frankia myöhemmin \"mieheksi, joka näytti yllättyneeltä "
            "julkisen liikenteen käsitteestä.\"",
        ],
    },
    "death_rooftop_fall": {
        "texts": [
            "Frank hyppää. Hetken hän on Kallion vapain mies. "
            "Painovoima ei kuitenkaan ole kiinnostunut vapaudesta. "
            "Painovoima on kiinnostunut fysiikasta.",
            "Kuja ottaa hänet vastaan betonin vieraanvaraisuudella. "
            "Kolme kerrosta ei ole pitkä pudotus, mutta se on tarpeeksi pitkä.",
        ],
    },
    "death_metro_crash": {
        "texts": [
            "Frank työntää vivun eteen. Juna vastaa "
            "innostuneesti. Tunnelin seinä vastaa lopullisuudella.",
            "Helsingin metro raportoi myöhemmin pienestä huoltotapahtumasta. "
            "Frank, josta on tullut osa infrastruktuuria, "
            "ei ole käytettävissä kommenteille.",
        ],
    },
    "death_limo_police": {
        "texts": [
            "Valo on punainen. Kuljettaja ajaa päin. Poliisiauto, joka on "
            "istunut risteyksessä suomalaisen talven kärsivällisyydellä, "
            "seuraa perässä.",
            "Kaksi Frankia varastetussa limusiinissa ajamassa päin punaista kello 3 yöllä. "
            "Poliisiraportti kirjoittaa itsensä. Tuomari ei tarvitse kauaa.",
        ],
    },
    "death_coast_guard": {
        "texts": [
            "Frank kiipeää rahtilaivan portaita. Hän ehtii kolme askelta "
            "ennen kuin taskulamppu löytää hänet. Rajavartija "
            "näyttää väsyneeltä. Frank näyttää kiinni jääneeltä.",
            "Laiva oli menossa Lyypekkiin. Frank on menossa pidätysselliin. "
            "Lyypekki ei ole Eira, mutta selli ei myöskään ole. Ainakin sellissä "
            "on lämmin.",
        ],
    },
    "death_senate_patrol": {
        "texts": [
            "Frank istuu tuomiokirkon portaille. Kivi on kylmä. "
            "Hänen silmänsä sulkeutuvat vain hetkeksi.",
            "Partioauto löytää hänet kello 4, nukkumasta pylvästä vasten "
            "kuin pyhimys, joka on luopunut ihmeistä. Poliisit ovat "
            "lempeät. Käsiraudat eivät ole.",
        ],
    },

    # Eksymiset
    "lost_woman": {
        "texts": [
            "Hän keittää kahvia. Asunto on lämmin. Siellä on kissa. "
            "Kissa ei välitä Eirasta.",
            "Frank istuu. Hän ei nouse enää. Kahvi korvautuu "
            "illallisella, illallinen aamupalalla, aamupala vuosilla.",
            "Frank ei koskaan saavuttanut Eiraa. Mutta ehkä Eira ei ollut "
            "koskaan tarkoitettu saavutettavaksi. Ehkä se oli aina keittiö, "
            "kissa ja kahvi, jonka joku muu keitti.",
        ],
    },
    "lost_drunk": {
        "texts": [
            "Juopon laulu on tango. Frank tietää sanat. "
            "Ei pitäisi, mutta tietää. He laulavat yhdessä. "
            "Laulussa on neljäkymmentä säkeistöä.",
            "Jossain kolmannenkymmenenseitsemännen kohdalla Frank unohtaa Eiran. "
            "Neljännenkymmenennen kohdalla hän unohtaa kaiken.",
            "Hän herää Kalliossa. On aamu. Matka on ohi "
            "ennen määränpäätä. Tango jatkuu.",
        ],
    },
    "lost_bench": {
        "texts": [
            "Penkki on mukava sillä tavalla, jolla väsymys tekee "
            "mistä tahansa mukavaa. Frank sulkee silmänsä yhdeksi hetkeksi.",
            "Aamu löytää hänet yhä sieltä. Puisto on täynnä lenkkeilijöitä "
            "ja koiranulkoiluttajia ja ihmisiä, jotka pääsivät perille "
            "tunteja sitten.",
            "Frank ei koskaan saavuttanut Eiraa. Hän saavutti penkin. "
            "Jotkut matkat päättyvät sinne, minne väsymys päättää.",
        ],
    },
    "lost_kamppi": {
        "texts": [
            "Länsi. Kamppi. Linja-autoasema. Paikka, josta lähdetään, "
            "ei johon saavutaan. Frank on sekoittanut suuntansa.",
            "Hän nousee bussiin. Se menee Espooseen. Espoo ei ole Eira. "
            "Espoo ei ole oikeastaan mitään.",
            "Frank ei koskaan saavuttanut Eiraa. Hän saavutti lähiön. "
            "Tämä on surullisin loppu kaikista.",
        ],
    },
    "lost_cafe": {
        "texts": [
            "Frank tilaa toisen kahvin. Tarjoilija, joka on nähnyt tämän "
            "ennenkin, ei sano mitään. Kahvi tulee. Se on identtinen "
            "edellisen kanssa.",
            "Tunteja kuluu. Muut Frankit lähtevät yksi kerrallaan kohti "
            "määränpäitä, joita he ehkä saavuttavat tai eivät. Frank jää. "
            "Kahvi jää.",
            "Hän on yhä siellä aamulla, kun päivävuoro saapuu "
            "ja yöstä tulee tarina, jota kukaan ei kerro. Eira on etelässä. "
            "Kahvila on täällä. Joitain etäisyyksiä ei voi ylittää kofeiinilla.",
        ],
    },
    "lost_ferry": {
        "texts": [
            "Lauttaterminaali on valoisa ja lämmin ja täynnä ihmisiä, jotka ovat "
            "menossa Tukholmaan. Tukholma ei ole Eira. Tukholma ei ole edes "
            "Helsinki. Mutta lautta lähtee kahdenkymmenen minuutin kuluttua ja Frank "
            "on kyllästynyt kävelemään.",
            "Hän nousee laivaan. Itämeri on musta ja valtava ja välinpitämätön. "
            "Frank seisoo kaiteella ja katsoo Helsingin kutistuvan.",
            "Hän ei koskaan saavuttanut Eiraa. Hän saavutti tax free -myymälän. "
            "Vodka on halvempaa täällä, mikä on suomalaisin "
            "saatavilla oleva lohdutus.",
        ],
    },
    "lost_kiosk": {
        "texts": [
            "Frank tilaa nakin. Se tulee sämpylässä sinapin kera. "
            "Hän syö sen seisten, suomalaisessa perinteessä, jossa ruokaa "
            "nautitaan tunnustamatta nautintoa.",
            "Hän tilaa toisen. Ja kolmannen. Kioskimies, joka on työskennellyt "
            "öitä seitsemäntoista vuotta, tunnistaa ilmeen. Se on sellaisen "
            "miehen ilme, joka on lakannut kävelemästä.",
            "Frank ei koskaan saavuttanut Eiraa. Hän saavutti kioskin. Eira on kahden "
            "korttelin päässä etelässä, mutta kaksi korttelia on äärettömyys, kun jalat ovat "
            "päättäneet neuvotella.",
        ],
    },
}

# --- Finnish free version (Kaurismäki-versio) ---
# Written fresh in Finnish, not translated from English.

SCENES_FI2 = {
    "intro": {
        "texts": [
            "Helsinki. Myöhäinen yö. Tai varhainen aamu. "
            "Kellolla ei ole väliä, kun ei ole töihin menoa.",
            "Kalliossa, baarissa, istuu joukko Frankeja. Heillä on yhteinen "
            "nimi ja yhteinen usko: jossakin on paremmin. Se paikka on Eira.",
            "Mukana on myös Pekka. Pekka ei ole Frank. Pekka puhuu englantia. "
            "Kukaan ei tiedä miksi.",
            "Tänä yönä he lähtevät. Jotkut pääsevät perille. "
            "Jotkut kuolevat. Jotkut unohtavat minne olivat menossa.",
            "Sinä olet Frank.",
        ],
        "choices": ["Aloita matka"],
    },

    "ch01_bar": {
        "texts": [
            "Baarilla on nimi, mutta kyltissä lukee vain \"Baari\". Se riittää.",
            "Pöydän ääressä istuu useita Frankeja. Kukaan ei puhu mitään "
            "tärkeää. Yksi juo hitaasti, kuten mies joka tietää ettei kotona "
            "odota kukaan. Pekka lukee Hesaria ylösalaisin. Ilmeisesti tahallaan.",
            "\"Eira\", sanoo yksi Frankeista. Muut nyökkäävät. Suunnitelma "
            "on valmis. Yksityiskohtia ei ole, mutta se on suunnitelman "
            "ongelma, ei heidän.",
        ],
        "choices": [
            "Lähde etuovesta",
            "Kokeile takaovea",
            "Tilaa vielä yksi",
            "Häiritse Pekkaa",
        ],
        "extras": {
            "pekka_advice": "Pekka laskee lehden. \"The thing about Eira,\" "
                "hän sanoo englanniksi, \"is that it exists.\" "
                "Hän nostaa lehden takaisin. Lisää ei tule.",
            "pekka_choice": "Lähde etuovesta",
        },
    },

    "ch02_alley": {
        "texts": [
            "Kuja. Betoni, sade, kissa joka tuijottaa ikkunasta. "
            "Kissa on oppinut olemaan reagoimatta.",
            "Roskisten takana kyyhötti mies tummassa takissa. Frank. "
            "Nousi ylös, katsoi.",
            "\"Poliiseja\", hän sanoo. \"Joka puolella. Kuin sieniä "
            "sateen jälkeen, mutta paremmin palkattuja.\"",
        ],
        "choices": [
            "Suuntaa pääkadulle",
            "Oikaise sisäpihan kautta",
            "Takaisin baariin",
        ],
    },

    "ch02_dumpster": {
        "texts": [
            "Takaovi. Kuja. Roskiksia neljä kappaletta ja haju "
            "joka ansaitsee erillisen maininnan.",
            "Frank seisoi roskiksen vieressä, käsi sisällä kuin eläinlääkäri. "
            "Veti esiin paperin. Tutki sitä.",
            "\"Kartta\", hän sanoi. \"Kai. Voi olla myös ruokalista. "
            "Tässä valossa kadut ja keitot näyttävät samalta.\"",
        ],
        "choices": [
            "Ota kartta",
            "Jätä hänet hommiin",
        ],
        "extras": {
            "map_taken": "Frank otti kartan. Se oli kostea ja haisi "
                "kahvinporoilta. Jotkut kadut oli merkitty nimellä. "
                "Jotkut ei. Parempaa ei ollut tarjolla.",
            "map_choice": "Jatka kohti Hämeentietä",
        },
    },

    "ch03_hameentie": {
        "texts": [
            "Hämeentie. Pitkä, märkä, suora kuin päätös josta ei voi "
            "perääntyä. Raitiovaunukiskot kiiltivät mutta ratikka ei näkynyt. "
            "Ratikka ei koskaan näy.",
            "Parkkeeratun Ladan vieressä seisoi Frank ja henkari. "
            "Henkari oli väärässä muodossa. Frank oli oikeassa paikassa "
            "väärästä syystä.",
        ],
        "choices": [
            "Auta varastamaan auto",
            "Kävele kiskoja pitkin",
            "Suuntaa Sörnäisten metroon",
        ],
    },

    "ch03_courtyard": {
        "texts": [
            "Sisäpiha. Hiljaisuus joka tuntuu tahalliselta. "
            "Pyykit roikkuivat märkinä naruilla.",
            "Kolmannessa kerroksessa ikkuna valaistu. Nainen. "
            "Nojasi ulos, sanoi jotain. Ehkä tervehdys. "
            "Ehkä kysymys. Ehkä kumpikin.",
        ],
        "choices": [
            "Puhu hänelle",
            "Kiipeä palotikkaita katolle",
            "Piiloudu ja odota",
        ],
        "extras": {
            "frank_fence": "Frank odotti. Varjossa, paikallaan. "
                "Sitten aidan yli tuli toinen Frank, kuin olisi sovittu. "
                "Ei ollut sovittu.",
            "fence_choice": "Jatka yhdessä metroa kohti",
        },
    },

    "ch03_rooftop": {
        "texts": [
            "Palotikkaat johtivat katoille. Ne oli rakennettu optimismilla "
            "joka oli jo haihtunut.",
            "Katolta Kallio levittäytyi joka suuntaan — lähiö joka pitää "
            "itsensä kaupunkina. Etelässä valoja. Tuuli toi savun ja jotain "
            "muuta, ehkä toivon, ehkä pakokaasun.",
            "Viereinen rakennus oli kahden metrin päässä. Kaksi metriä on "
            "joko vähän tai paljon riippuen siitä, mitä on menettämässä.",
        ],
        "choices": [
            "Kiipeä alas kadulle",
            "Hyppää viereiselle katolle",
            "Hyppää kujalle",
        ],
    },

    "ch04_car": {
        "texts": [
            "Lada käynnistyi neljännellä yrityksellä. "
            "\"Hyvä auto\", sanoi Frank. Toisella Frankilla ei ollut kommenttia.",
            "Helsinki ajettuna on eri kaupunki. Pimeä ja pienempi, "
            "mutta myös suurempi. Ladan ajovaloissa kaikki näytti "
            "vähän kellertävältä.",
            "Hakaniemen kohdalla moottori yskäisi kerran ja kuoli. "
            "Ei dramaattisesti. Lopetti vain.",
        ],
        "choices": [
            "Jatka jalan torin kautta",
            "Yritä korjata autoa",
        ],
    },

    "ch04_metro": {
        "texts": [
            "Metroasema. Loisteputket, kaakeliseinät, rullaportaat "
            "jotka laskevat hitaammin kuin haluaisi. Institutionaalinen "
            "tunnelma kuin sairaalassa, mutta ilman odotusta paranemisesta.",
            "Penkillä istui Frank ja poltti. Tupakointikielto-kyltti oli "
            "joko rikki tai hän ei välittänyt siitä. Tuijotti tyhjille raiteille.",
            "\"Junia ei tule\", hän sanoi. \"Ei tunteihin. Ehkä ei enää "
            "koskaan. Vaikea sanoa eroa.\" Tauko. \"On tosin yksi. "
            "Perällä. Huoltojuna. Vain seisoo.\"",
        ],
        "choices": [
            "Odota junaa joka tapauksessa",
            "Kävele tunneliin",
            "Kävele huoltojunan luo",
            "Nouse takaisin ylös",
        ],
        "extras": {
            "wait_text": "Frank istui. Penkki oli kova. Loisteputket "
                "hurisivat yhtä ainoaa säveltä, joka ei ole sävel. "
                "Juna ei tullut. Juna ei ollut tulossa.",
            "wait_choice": "Kävele tunneliin",
        },
    },

    "ch04_metro_train": {
        "texts": [
            "Laiturin perällä seisoi huoltojuna. Se näytti siltä kuin "
            "se olisi aina seissyt siellä ja aina seisoisi.",
            "Ovi oli auki. Ohjainlaite yksinkertainen. Frank istui "
            "kuljettajan paikalla ja katsoi mittaristoa kuin olisi lukenut "
            "menua josta ei tunnistanut yhtä ainutta ruokaa.",
            "\"Ajoin kerran trukkia\", hän sanoi. \"Sama idea.\" "
            "Se ei ole sama idea.",
        ],
        "choices": [
            "Anna hänen ajaa",
            "Ota itse ohjaimet",
            "Poistu ja kävele tunnelissa",
        ],
        "extras": {
            "let_drive_1": "Frank istui matkustajan paikalle. Toinen Frank "
                "työnsi vipua. Juna heräsi, murahti ja lähti liikkeelle "
                "kuten virkamies maanantaiaamuna.",
            "let_drive_2": "Tunneli vieri ohi. Asemat ilmestyivät ja "
                "katosivat kuin lupaukset. Kuljettaja hyräili jotain "
                "tuntematonta. Juna nousi ylös sataman suuntaan.",
            "let_drive_choice": "Poistu satamassa",
        },
    },

    "ch05_tunnels": {
        "texts": [
            "Tunneli nielee valon täydellisesti ja ilman katumusta. "
            "Vesi tippuu katosta. Rytmi on lähes musiikillinen, "
            "jos pitää siitä lajista.",
            "Syvemmältä ilmestyi Frank pimeydestä kuin sieltä olisi tilattu. "
            "Kolme päivää täällä, hän väitti. Kello pysähtyi tiistaina. "
            "Tänään on ehkä perjantai.",
            "\"Tiedän tien\", hän sanoi. Silmät sanoivat muuta. "
            "Pimeässä kaikki suunnat tuntuvat yhtä oikeilta.",
        ],
        "choices": [
            "Seuraa hänen ohjeitaan",
            "Mene omaa tietä",
            "Käänny takaisin",
        ],
    },

    "ch05_cafe": {
        "texts": [
            "Kahvila oli auki koska se aina on. "
            "Valot päänsäryn värisiä. Kahvi oikean lämpöistä väärällä hetkellä.",
            "Neljä Frankia istui neljässä pöydässä ja teeskenteli "
            "etteivät nähneet toisiaan. Se vaati enemmän vaivaa kuin näytti.",
            "Viides Frank astui sisään, ravisti vettä takistaan. Nyökkäsi. "
            "\"Minulla on auto\", hän sanoi. \"Limusiini. No. Pitkä auto. "
            "Filosofinen ero.\"",
        ],
        "choices": [
            "Lähde Frankin ja auton mukaan",
            "Lähde takaovesta torille",
            "Jää vielä kahville",
        ],
    },

    "ch05_harbor": {
        "texts": [
            "Sörnäisten satama. Diesel, kala, ja se erityinen surullisuus "
            "joka kuuluu teollisuusmaisemaan yöllä. Nosturit seisoivat "
            "taivaanrantaa vasten kuin ne odottivat jotain.",
            "Frank nojasi pollariin ja poltti. Sellaisen miehen ilmeellä "
            "joka on odottanut laivaa joka ei tule. "
            "Helsingissä se on monella sama ilme.",
            "\"Laivat menevät Tallinnaan\", hän sanoi. "
            "\"Mutta Tallinna ei ole Eira.\" Tauko. "
            "\"Mikään ei ole Eira. Se on koko ongelma.\"",
        ],
        "choices": [
            "Seuraa rantaviivaa etelään",
            "Oikaise sisämaahan kahvilan suuntaan",
            "Yritä nousta rahtilaivaan",
        ],
    },

    "ch06_market": {
        "texts": [
            "Hakaniemen tori. Kojut kiinni, lukittu. "
            "Humalainen mies istui arkun päällä ja lauloi jotain "
            "jolla oli enemmän säkeistöjä kuin tarkoitusta.",
            "Kojun takaa ilmestyi Frank, ja hänen kanssaan Pekka. "
            "Pekka sanoi jotain englanniksi taloudesta tai filosofiasta. "
            "Kukaan ei pyytänyt.",
            "Etelässä siltoja. Niiden alla musta vesi, joka ei kommentoi.",
        ],
        "choices": [
            "Ylitä Pitkäsilta",
            "Kulje Siltasaaren kautta",
            "Seuraa laulavaa juoppoa",
        ],
    },

    "ch06_limo": {
        "texts": [
            "Auto oli pitkä ja musta ja muistutti ajasta ennen kuin "
            "auto-käsite muuttui. Sisätiloissa kuusenraikastin ja hiljaisuus.",
            "Frank istui takapenkille. Toinen Frank ajoi. "
            "Ohi liukui katuja joita Frank ei tunnistanut, "
            "vaikka Helsinki ei ole iso kaupunki.",
            "\"Minne?\" kuljettaja kysyi kahden kilometrin jälkeen. "
            "Suunnittelemattomuus on kansallinen ominaisuus.",
        ],
        "choices": [
            "\"Etelään. Tuomiokirkolle.\"",
            "\"Jätä minut Kruununhakaan\"",
            "\"Aja päin punaista, minulla on kiire\"",
        ],
    },

    "ch07_park": {
        "texts": [
            "Kaisaniemen puisto. Puut seisovat kuten puut seisovat — "
            "paikallaan, ilman valituksia. Kaukaa kuului meren ääni. "
            "Tai liikenteen.",
            "Helsingissä ero on pieni.",
            "Penkillä nukkui Frank, takki korviin vedettynä. "
            "Hengitti tasaisesti. Se oli rauhallisin asia koko yössä.",
        ],
        "choices": [
            "Herätä hänet, jatka yhdessä",
            "Anna hänen nukkua, jatka yksin",
            "Lepää penkillä sinäkin",
        ],
    },

    "ch07_katajanokka": {
        "texts": [
            "Katajanokka. Punainen tiili, raudan haju, suurlähetystöjä "
            "jotka nukkuvat porttien takana. "
            "Katuvalo ei paljasta mitään tarpeetonta.",
            "Frank seisoi Jäänmurtajamuseon edessä ja luki kylttiä "
            "jota hän ei nähnyt pimeässä. \"Tiesit siitä\", hän sanoi, "
            "\"että jäänmurtajat murtavat jään omalla painollaan?\" "
            "Tauko. \"Kuin vuokranantajat.\"",
            "Etelässä Uspenskin katedraalin siluetti. Sen takana Esplanadi.",
        ],
        "choices": [
            "Jatka etelään kohti Esplanadia",
            "Kävele tuomiokirkon aukiolle",
            "Suuntaa lauttaterminaaliin",
        ],
    },

    "ch08_kruununhaka": {
        "texts": [
            "Kruununhaka. Rakennukset isompia, siistimpiä, vanhempia. "
            "Ne katsovat alaspäin tavalla joka ei ole arkkitehtoninen valinta.",
            "Arkkitehtuuri kertoo rahasta ja historiasta. "
            "Molemmat ovat Kruununhaan vanhoja asukkaita. Frank ei ole.",
            "Poliisiauto liukui kadulla kuin hai matalassa vedessä, "
            "valot pois päältä. Tarkoitus on selvä.",
        ],
        "choices": [
            "Väistä oviaukkoon",
            "Kävele kuin ei mitään",
            "Juokse",
        ],
        "extras": {
            "police_pass": "Frank käveli. Poliisiauto ohitti. Sen miehistö "
                "joi kahvia ja kiistelivät jalkapallosta. He eivät "
                "katsoneet Frankia. Frank ei katsonut heitä. "
                "Kaksi laivaa yössä, molemmat tietäen toisen läsnäolosta.",
            "police_choice": "Jatka Esplanadille",
        },
    },

    "ch08_senate_square": {
        "texts": [
            "Senaatintori. Tuomiokirkko valkoinen, suuri, täsmälleen "
            "sellainen kuin Jumala tilaisi jos tilaisi. "
            "Portaat riittävät armeijalle. Tänä yönä pelkkiä "
            "kyyhkysiä ja hiljaisuutta.",
            "Portaiden juuressa Aleksanteri II:n patsas katsoo tyhjää "
            "toria. Hän on seissyt siinä sata kolmekymmentä vuotta. "
            "Kasvoilla se ilme kun on ollut väärässä kauan aikaa "
            "mutta ei voi lähteä.",
            "Kadut viettyvät etelään. Kohti merta, Esplanadia "
            "ja sitä mikä voisi olla Eira.",
        ],
        "choices": [
            "Ylitä tori etelään kohti Esplanadia",
            "Kävele itään kohti Katajanokkaa",
            "Istu portailla ja lepää",
        ],
    },

    "ch09_esplanadi": {
        "texts": [
            "Esplanadi. Leveä, puita, penkkejä. Ensimmäistä kertaa "
            "tänä yönä meren haju — suola, diesel, mahdollisuus.",
            "Kaksi Frankia kiistelivät. \"Eira on etelässä.\" "
            "\"Eira on käsite.\" He olivat kiistäneet Kalliosta asti.",
            "\"Molemmat voivat olla oikeassa\", sanoi kolmas Frank "
            "jota ei ollut aiemmin ollut. Kukaan ei kysynyt mistä hän tuli.",
        ],
        "choices": [
            "Mene etelään kohti Kaivopuistoa",
            "Mene länteen kohti Kamppia",
            "Seuraa riiteleviä Frankeja",
            "Ota Bulevardi",
        ],
        "extras": {
            "follow_south": "Frankit lopettivat kiistelyn ja kävelivät etelään. "
                "Frank seurasi. Kiistely jatkui, hiljempaa, "
                "kuin meri jo rauhoittaisi heitä.",
            "follow_south_choice": "Jatka etelään",
            "follow_west": "Frankit kääntyivät länteen. \"Oikotie\", sanoi toinen. "
                "Frank seurasi. Oikotie päättyy Kamppiin.",
            "follow_west_choice": "...",
        },
    },

    "ch09_bulevardi": {
        "texts": [
            "Bulevardi. Nimi kuulostaa ranskalaiselta mutta katu on "
            "suomalainen: pitkä, hiljainen, menossa jonnekin kertomatta.",
            "Kulmassa kioski loisti kuin majakka niille jotka ovat "
            "kadottaneet kompassin. Mies osti makkaraa. Toinen mies katsoi. "
            "Helsinki yöllä.",
            "Frank nojasi lyhtypylvääseen, katsoi bussiaikataulua. "
            "\"Eira on tuolla\", hän sanoi osoittaen pimeyteen. "
            "\"Kaksi korttelia. Ehkä kolme. Yöllä matkat venyvät.\"",
        ],
        "choices": [
            "Jatka kohti Eiraa",
            "Pysähdy kioskilla",
            "Oikaise Kaivopuiston kautta",
        ],
    },

    "ch10_kaivopuisto": {
        "texts": [
            "Kaivopuisto. Meri vihdoin oikeasti läsnä, ei vain mainittuna. "
            "Tähdet näkyivät. Tuuli toi suolaa.",
            "Frank seisoi rannalla. Hänen siluettinsa oli se asia "
            "Suomessa joka selittää kaiken muun.",
            "Lännessä Eira. Ehkä kaksi korttelia. Ehkä kolme. "
            "Valot jotka eivät ole Kallio.",
        ],
        "choices": [
            "Kävele rantaa pitkin kohti Eiraa",
            "Istu Frankin viereen",
            "Kulje katua pitkin",
        ],
        "extras": {
            "talk_1": "Frank istui. Toinen Frank ei puhunut. Meri ei puhunut. "
                "Hiljaisuus oli suomalaista — ei köyhää eikä rikasta, vain tarkka.",
            "talk_2": "Lopulta toinen Frank nousi, nappasi napit kiinni "
                "ja käveli veteen. Ei hukuakseen. Vain kävelemään, "
                "kuten miehellä olisi asiaa.",
            "talk_3": "Frank katsoi kunnes toinen katosi. Sitten kääntyi "
                "länteen. Koska Frankit kävelevät. Se on heidän luonteensa.",
            "talk_choice": "Kävele kohti Eiraa",
        },
    },

    "eira": {
        "texts": [
            "Eira.",
            "Taivas muuttui. Ei vielä aurinko — se tulisi myöhemmin — "
            "mutta pimeys oli jo väsynyt. Jugend-talot seisoivat siisteinä "
            "kuten talot joille ei ole tapahtunut mitään pahaa.",
            "Meri oli siinä. Aallot koskettivat kiviä varoen, "
            "kuten vieras joka ei tiedä onko tervetullut.",
            "Olit Eirassa.",
            "Se näytti Helsingiltä.",
            "Mutta oli Eira. Ja se riitti. "
            "Tai ainakin se oli kaikki mitä oli.",
        ],
    },

    # Kuolemat

    "death_bar_raid": {
        "texts": [
            "Yhdestä juomasta tuli kaksi. Kahdesta tuli hiljaisuus. "
            "Kolmannen kohdalla tuli poliisi.",
            "Frankin matka päättyi baariin. Symmetriaa siinä. "
            "Poliisi ei arvosta symmetriaa.",
        ],
    },
    "death_bar_return": {
        "texts": [
            "Baari oli täynnä poliiseja. He joivat lämmintä olutta "
            "ja katselivat ympäriinsä kuten ammattilaiset.",
            "Taaksepäin ei mennä. Frank tiesi sen. Meni silti.",
        ],
    },
    "death_car_fix": {
        "texts": [
            "Frank avasi konepellin. Moottori katsoi häntä takaisin — "
            "monimutkainen, välinpitämätön, ratkaisematon.",
            "Poliisi saapui ennen kuin Frank keksi mitään. "
            "Lada kuoli konepelti auki. Ainakin se kuoli rehellisesti.",
        ],
    },
    "death_tram_tracks": {
        "texts": [
            "Frank käveli kiskoja pitkin. Ratikka ei kuulu näin myöhään, "
            "hän ajatteli. Kiskot olivat tyhjiä. Yö oli hiljainen.",
            "Ratikka kuului.",
            "Kuljettaja, joka oli ajanut tätä reittiä kahdeksan vuotta, "
            "kuvaili myöhemmin Frankia \"mieheksi joka näytti yllättyneeltä, "
            "että Helsingissä on julkinen liikenne.\"",
        ],
    },
    "death_rooftop_fall": {
        "texts": [
            "Frank hyppäsi. Hetken hän oli vapaa. "
            "Painovoima ei ole kiinnostunut vapaudesta.",
            "Kuja otti hänet vastaan betonin kohteliaisuudella. "
            "Kolme kerrosta ei ole pitkä matka. Riittää kuitenkin.",
        ],
    },
    "death_metro_crash": {
        "texts": [
            "Frank työnsi vipua eteenpäin. Juna innostui. "
            "Tunnelin seinä ei.",
            "Helsingin metro kirjasi myöhemmin pienen huoltopoikkeaman. "
            "Frank, josta oli tullut osa infrastruktuuria, "
            "ei ollut tavoitettavissa kommenttia varten.",
        ],
    },
    "death_limo_police": {
        "texts": [
            "Valo oli punainen. Kuljettaja ajoi läpi. Poliisiauto, "
            "joka oli odottanut risteyksessä koko yön, "
            "ei jäänyt odottamaan enempää.",
            "Kaksi Frankia varastetussa limusiinissa, päin punaista, "
            "kello kolme yöllä. Poliisiraportti kirjoittaa itsensä. "
            "Tuomari ei tarvitse kauaa.",
        ],
    },
    "death_coast_guard": {
        "texts": [
            "Frank kiipesi laivaan. "
            "Pääsi kolme askelta ennen kuin taskulamppu löysi hänet.",
            "Laiva meni Lyypekkiin. Frank meni säilöön. "
            "Lyypekki ei ole Eira, mutta säilökään ei ole. "
            "Ainakin säilössä on lämmin.",
        ],
    },
    "death_senate_patrol": {
        "texts": [
            "Frank istui portaille. Kivi oli kylmä. "
            "Silmät painuivat kiinni vain hetkeksi.",
            "Partioauto löysi hänet aamuneljältä nukkumassa "
            "pylvästä vasten kuin pyhimys joka on luopunut ihmeistä. "
            "Poliisit olivat ystävällisiä. Käsiraudat eivät olleet.",
        ],
    },
    "death_tunnel_train": {
        "texts": [
            "Frank valitsi oman tien. "
            "Pimeässä kaikki tiet tuntuvat yhtä hyviltä.",
            "Kuljettaja ei nähnyt Frankia. Frank ei nähnyt kuljettajaa. "
            "Kaksi tuntematonta samassa tunnelissa, lyhyesti.",
        ],
    },
    "death_police_stop": {
        "texts": [
            "\"Käyttäydy luonnollisesti\" toimii vain niille jotka tietävät "
            "miltä luonnollinen näyttää. Frank Kruununhaassa kello kolme "
            "yöllä pitkässä takissa ei näytä luonnolliselta.",
            "Poliisit olivat kohteliaita. Se teki asiasta pahemman.",
        ],
    },
    "death_police_run": {
        "texts": [
            "Frank juoksi. Poliisi juoksi perässä. Frank oli nopea "
            "mutta yö oli nopeampi, ja jalkakäytävä otti hänet kiinni "
            "suomalaisen talven tarkkuudella.",
            "Juoksemista poliisilta karkuun Kruununhaassa. "
            "Enemmän liikuntaa kuin tämä kaupunginosa on nähnyt pitkään aikaan.",
        ],
    },
    "death_street_patrol": {
        "texts": [
            "Katu vie suoraan poliisin tiesulun läpi. "
            "He olivat odottaneet koko yön juuri sellaista Frankia.",
            "Niin lähellä Eiraa. Meren haju kantautui. "
            "Mutta meri tuoksuu samalta poliisiautostakin.",
        ],
    },

    # Eksymiset

    "lost_woman": {
        "texts": [
            "Hän keitti kahvia. Asunto oli lämmin. Siellä oli kissa. "
            "Kissa ei tiennyt Eirasta eikä välittänyt tietää.",
            "Frank istui. Hän ei noussut enää. Kahvi vaihtui illalliseksi, "
            "illallinen aamupalaksi, aamupala vuosiksi.",
            "Frank ei koskaan saavuttanut Eiraa. Ehkä Eira oli aina tämä: "
            "lämmin keittiö, vieras kissa, kahvi jonka joku muu keitti.",
        ],
    },
    "lost_drunk": {
        "texts": [
            "Juopon laulu oli tango. Frank tiesi sanat, vaikka ei "
            "olisi pitänyt. He lauloivat yhdessä. "
            "Laulussa oli neljäkymmentä säkeistöä.",
            "Kolmenkymmenenseitsemännen säkeistön kohdalla Frank "
            "unohti Eiran. Neljännenkymmenennen kohdalla hän unohti kaiken.",
            "Hän heräsi Kalliossa. Aamu. Matka oli ohi ennen kuin "
            "se päättyi. Tango jatkui.",
        ],
    },
    "lost_bench": {
        "texts": [
            "Penkki oli mukava väsymyksen tavalla. "
            "Frank sulki silmät hetkeksi.",
            "Aamu löysi hänet siitä. Puisto täynnä koiranulkoiluttajia "
            "ja lenkkeilijöitä ja ihmisiä joilla oli mihin mennä.",
            "Frank ei koskaan saavuttanut Eiraa. Hän saavutti penkin. "
            "Jotkut matkat päättyvät sinne minne jalat päättävät.",
        ],
    },
    "lost_kamppi": {
        "texts": [
            "Länsi. Kamppi. Linja-autoasema. Paikka, josta lähdetään, "
            "ei johon saavutaan. Frank oli sekoittanut suuntansa.",
            "Hän nousi bussiin. Se meni Espooseen. "
            "Espoo ei ole Eira. Espoo ei oikein ole mitään.",
            "Frank ei koskaan saavuttanut Eiraa. Hän saavutti lähiön. "
            "Tämä on surullisin loppu.",
        ],
    },
    "lost_cafe": {
        "texts": [
            "Frank tilasi toisen kahvin. Tarjoilija, joka oli nähnyt "
            "tämän aiemmin, ei sanonut mitään. Kahvi tuli. Sama kahvi.",
            "Muut Frankit lähtivät yksi kerrallaan. Frank jäi. Kahvi jäi.",
            "Hän oli siellä vielä aamulla kun päivävuoro tuli. "
            "Eira on etelässä. Kahvila on tässä. "
            "Jotkut etäisyydet ovat liian pitkiä kahville.",
        ],
    },
    "lost_ferry": {
        "texts": [
            "Lauttaterminaali oli valoisa, lämmin, täynnä ihmisiä "
            "joilla oli lippu Tukholmaan. Tukholma ei ole Eira. "
            "Tukholma ei ole edes Helsinki. "
            "Mutta lautta lähtee kahdessakymmenessä minuutissa.",
            "Hän nousi laivaan. Itämeri oli musta, laaja ja kiinnostumaton. "
            "Frank seisoi kannella ja katsoi Helsingin pienenevän.",
            "Hän ei koskaan saavuttanut Eiraa. "
            "Hän saavutti tax free -myymälän. "
            "Viina on halvempaa, mikä on suomalaisin lohdutus mitä on.",
        ],
    },
    "lost_kiosk": {
        "texts": [
            "Frank tilasi makkaran. Se tuli sämpylässä sinapin kera. "
            "Hän söi sen seisten, suomalaisessa perinteessä "
            "jossa ruoka syödään tunnustamatta nautintoa.",
            "Hän tilasi toisen. Sitten kolmannen. Kioskimies, "
            "joka oli tehnyt yövuoroja seitsemäntoista vuotta, "
            "tunnisti ilmeen. Ilme miehellä, joka on lakannut kävelemästä.",
            "Frank ei koskaan saavuttanut Eiraa. "
            "Eira on kaksi korttelia etelässä. "
            "Kaksi korttelia on ääretön matka kun jalat ovat kieltäytyneet.",
        ],
    },
}
