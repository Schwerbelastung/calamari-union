"""
All narrative text for Calamari Union.
Organized by scene ID. Each scene has description blocks and choice text.
Tone: deadpan, dry, minimal. Very Kaurismaki.
"""

SCENES = {
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
            "Ignore her and climb the fence",
            "Hide and wait",
        ],
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
            "Hard to tell the difference.\"",
        ],
        "choices": [
            "Wait for a train anyway",
            "Walk into the tunnel",
            "Take the escalator back up",
        ],
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
        ],
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
}
