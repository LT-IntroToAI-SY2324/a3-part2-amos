# the content of the movie database is taken from the textbook Concrete Abstractions: An
# Introduction to Computer Science Using Scheme, by Max Hailperin, Barbara Kaiser, and
# Karl Knight, Copyright (c) 1998 by the authors. Full text is available for free at
# http://www.gustavus.edu/+max/concrete-abstractions.html

# the Scheme file, Revision 1.3 as of 2005/12/20 14:09:37, has been reformated for
# Python. The original file is available as
# http://www.gustavus.edu/academics/mcs/max/concabs/code/movie.scm

# list of tuples w/ following format (the first tuple in the list is also annotated):
# each tuple contains title, director, year and actors/actresses
# `[(title, director, year, [actress_one, actor_two, ...]), ...]`
from typing import List, Tuple

movie_db: List[Tuple[str, str, int, List[str], str]] = [
    (
        "amarcord",  # title
        "federico fellini",  # director
        1974,  # year
        [
            "magali noel",
            "bruno zanin",
            "pupella maggio",
            "armando drancia",
        ],  # actors/actresses
        "7.9/10 on IMDB",
    ),
    (
        "the good, the bad, and the ugly",
        "sergio leone",
        1966,
        [
            "clint eastwood",
            "eli wallach",
            "lee van cleef",
        ],
        "8.8/10 on IMDB",
    ),
    (
        "halloween",
        "john carpenter",
        1978,
        [
            "donald pleasance",
            "jamie lee curtis",
            "tony moran",
            "nancy kyes",
            "charles cyphers",
        ],
        "7.7/10 on IMDB",
    ),
    (
        "friday the 13th",
        "sean s cunningham",
        1980,
        [
            "betsy palmer",
            "adrienne king",
            "jeannine taylor",
            "robbi morgan",
        ],
        "6.4/10 on IMDB",
    ),
    (
        "e.t. the extra-terrestrial",
        "steven spielburg",
        1982,
        [
            "henry thomas",
            "drew barrymore",
            "peter coyote",
            "dee wallace",
            "robert macnaughton"
        ],
        "7.9/10 on IMDB",
    ),
    (
        "home alone",
        "chris columbus",
        1990,
        [
            "macaulay culkin",
            "joe pesci",
            "daniel stern",
            "john heard",
        ],
        "7.7/10 on IMDB",
    ),
    (
        "the big easy",
        "jim mcbride",
        1987,
        [
            "dennis quaid",
            "ellen barkin",
            "ned beatty",
            "lisa jane persky",
            "john goodman",
            "charles ludlam",
        ],
        "6.5/10 on IMDB",
    ),
    (
        "boyz n the hood",
        "john singleton",
        1991,
        [
            "cuba gooding jr.",
            "ice cube",
            "larry fishburne",
            "tyra ferrell",
            "morris chestnut",
        ],
        "7.8/10 on IMDB",
    ),
    (
        "dead again",
        "kenneth branagh",
        1991,
        [
            "kenneth branagh",
            "emma thompson",
            "andy garcia",
            "derek jacobi",
            "hanna schygulla",
        ],
        "6.8 on IMDB",
    ),
    (
        "the godfather",
        "francis ford coppola",
        1972,
        ["marlon brando", "al pacino", "james caan", "robert duvall", "diane keaton"],
        "9.2/10 on IMDB",
    ),
    (
        "an american in paris",
        "vincente minnelli",
        1952,
        ["gene kelley", "leslie caron", "oscar levant", "nina foch", "george guetary"],
        "7.2/10 on IMDB",
    ),
    (
        "casablanca",
        "michael curtiz",
        1942,
        [
            "humphrey bogart",
            "ingrid bergman",
            "paul henreid",
            "claude rains",
            "sydney greenstreet",
            "peter lorre",
            "s z sakall",
            "conrad veidt",
            "dooley wilson",
        ],
        "8.5 on IMDB",
    ),
    (
        "citizen kane",
        "orson welles",
        1941,
        [
            "orson welles",
            "joseph cotten",
            "dorothy comingore",
            "ray collins",
            "george coulouris",
            "agnes moorehead",
            "ruth warrick",
        ],
        "8.3 on IMDB",
    ),
    (
        "gone with the wind",
        "victor fleming",
        1939,
        [
            "clark gable",
            "vivien leigh",
            "leslie howard",
            "olivia de havilland",
            "hattie mcdaniel",
            "butterfly mcqueen",
        ],
        "8.2 on IMDB",
    ),
    (
        "lawrence of arabia",
        "david lean",
        1962,
        [
            "peter otoole",
            "alec guinness",
            "anthony quinn",
            "jack hawkins",
            "jose ferrer",
            "omar sharif",
            "anthony quayle",
            "claude rains",
            "arthur kennedy",
            "donald wolfit",
        ],
        "8.3 on IMDB",
    ),
    (
        "the manchurian candidate",
        "john frankenheimer",
        1962,
        [
            "frank sinatra",
            "laurence harvey",
            "janet leigh",
            "angela lansbury",
            "henry silva",
            "james gregory",
            "leslie parrish",
            "john mcgiver",
            "khigh dhiegh",
            "james edwards",
        ],
        "7.9 on IMDB",
    ),
    (
        "metropolis",
        "fritz lang",
        1926,
        [
            "alfred abel",
            "gustay frohlich",
            "brigitte helm",
            "rudolf kleinrogge",
            "heinrich george",
        ],
        "8.3 on IMDB",
    ),
    (
        "othello",
        "orson welles",
        1952,
        [
            "orson welles",
            "michael mac liammoir",
            "robert coote",
            "suzanne cloutier",
            "faye compton",
            "doris dowling",
            "michael laurence",
        ],
        "7.5 on IMDB",
    ),
    (
        "spartacus",
        "stanley kubrick",
        1960,
        [
            "kirk douglas",
            "laurence olivier",
            "jean simmons",
            "charles laughton",
            "peter ustinov",
            "john gavin",
            "tony curtis",
            "woody strode",
        ],
        "7.9 on IMDB",
    ),
    (
        "a star is born",
        "george cuckor",
        1954,
        [
            "judy garland",
            "james mason",
            "jack carson",
            "tommy noonan",
            "charles bickford",
        ],
        "7.5 on IMDB",
    ),
    (
        "after the rehearsal",
        "ingmar bergman",
        1984,
        ["erland josephson", "ingrid thulin", "lena olin", "nadja palmstjerna-weiss"],
        "7.1 on IMDB",
    ),
    (
        "amadeus",
        "milos forman",
        1984,
        [
            "f murray abraham",
            "tom hulce",
            "elizabeth berridge",
            "simon callow",
            "roy dotrice",
            "christine ebersole",
            "jeffrey jones",
        ],
        "8.4 on IMDB",
    ),
    (
        "blood simple",
        "joel coen",
        1985,
        [
            "john getz",
            "frances mcdormand",
            "dan hedaya",
            "m emmet walsh",
            "samm-art williams",
        ],
        "7.6 on IMDB",
    ),
    (
        "chinatown",
        "roman polanski",
        1974,
        [
            "jack nicholson",
            "faye dunaway",
            "john huston",
            "perry lopez",
            "john hillerman",
            "darrell zwerling",
            "diane ladd",
            "roman polanski",
        ],
        "8.3 on IMDB",
    ),
    (
        "the cotton club",
        "francis ford coppola",
        1984,
        [
            "richard gere",
            "gregory hines",
            "diane lane",
            "lonette mckee",
            "bob hoskins",
            "james remar",
            "fred gwynne",
        ],
        "6.5 on IMDB",
    ),
    (
        "the crying game",
        "neil jordan",
        1992,
        [
            "stephen rea",
            "jaye davidson",
            "forest whitaker",
            "miranda richardson",
            "adrian dunbar",
            "breffini mckenna",
            "joe savino",
        ],
        "7.2 on IMDB",
    ),
    (
        "the day of the jackal",
        "fred zinnemann",
        1973,
        [
            "edward fox",
            "terence alexander",
            "michel auclair",
            "alan badel",
            "tony britton",
            "denis carey",
            "olga georges-picot",
            "cyril cusack",
        ],
        "7.8 on IMDB",
    ),
    (
        "diva",
        "jean-jacques beineix",
        1981,
        [
            "wilhelmenia wiggins fernandez",
            "frederic andrei",
            "richard bohringer",
            "thay an luu",
            "jacques fabbri",
            "chantal deruaz",
        ],
        "7.2 on IMDB",
    ),
    (
        "the dresser",
        "peter yates",
        1984,
        [
            "albert finney", 
            "tom courtenay", 
            "edward fox", 
            "zena walker",
        ],
        "7.5 on IMDB",
    ),
    (
        "el norte",
        "gregory nava",
        1983,
        [
            "zaide silvia gutierrez",
            "david villalpando",
            "ernesto gomez cruz",
            "alicia del lago",
            "trinidad silva",
        ],
        "7.7 on IMDB",
    ),
    (
        "the exorcist",
        "william friedkin",
        1973,
        [
            "ellen burstyn",
            "linda blair",
            "jason miller",
            "max von sydow",
            "kitty winn",
            "lee j cobb",
        ],
        "8.1 on IMDB",
    ),
    (
        "a fish called wanda",
        "michael chrichton",
        1988,
        [
            "john cleese",
            "jamie lee curtis",
            "kevin kline",
            "michael palin",
            "maria aitken",
            "tom georgeson",
            "patricia hayes",
        ],
        "7.5 on IMDB",
    ),
    (
        "flirting",
        "john duigan",
        1992,
        [
            "noah taylor",
            "thandie newton",
            "nicole kidman",
            "bartholomew rose",
            "felix nobis",
            "josh picker",
            "kiri paramore",
        ],
        "7.1 on IMDB",
    ),
    ("gates of heaven", "errol morris", 1978, [], "7.3 on IMDB"),
    (
        "house of games",
        "david mamet",
        1987,
        [
            "lindsay crouse",
            "joe mantegna",
            "mike nussman",
            "lilia skala",
            "j t walsh",
            "jack wallace",
        ],
        "7.2 on IMDB",
    ),
    (
        "iceman",
        "fred schepisi",
        1984,
        ["timothy hutton", "john lone", "lindsay crouse"],
        "6.1 on IMDB",
    ),
    (
        "jaws",
        "steven spielberg",
        1975,
        [
            "roy scheider",
            "robert shaw",
            "richard dreyfuss",
            "lorraine gary",
            "murray hamilton",
        ],
        "8.1 on IMDB",
    ),
    (
        "johnny got his gun",
        "dalton trumbo",
        1971,
        [
            "timothy bottoms",
            "kathy fields",
            "jason robards",
            "diane varsi",
            "donald sutherland",
            "eduard franz",
        ],
        "7.8 on IMDB",
    ),
    (
        "local hero",
        "bill forsyth",
        1983,
        [
            "burt lancaster",
            "peter reigert",
            "peter capaldi",
            "fulton mckay",
            "denis lawson",
        ],
        "7.3 on IMDB",
    ),
    (
        "the dark knight",
        "christopher nolan",
        2008,
        [
            "christian bale",
            "heath ledger",
            "gary oldman",
            "michael caine",
            "aaron eckhart",
            "morgan freeman",
        ],
        "9 on IMDB",
    ),
    (
        "malcolm x",
        "spike lee",
        1992,
        [
            "denzel washington",
            "angela basset",
            "albert hall",
            "al freeman jr",
            "delroy lindo",
            "spike lee",
        ],
        "7.7 on IMDB",
    ),
    (
        "killers of the flower moon",
        "martin scorsese",
        2023,
        [
            "leonardo dicaprio",
            "robert de niro",
            "lily gladstone",
            "jesse plemons",
        ],
        "9 on IMDB",

    ),
    (
        "interstellar",
        "christopher nolan",
        2014,
        [
            "matthew mcconaughey",
            "anne hathaway",
            "jessica chastain",
            "john lithgow",
        ],
        "8.7 on IMDB",
    ),
    (
        "oppenheimer",
        "christopher nolan",
        2023,
        [
            "cillian murphy",
            "emily blunt",
            "matt damon",
            "robert downey jr",
        ],
        "8.5 on IMDB",
    ),
    (
        "the wolf of wall street",
        "martin scorsese",
        2013,
        [
            "leonardo dicaprio",
            "margot robbie",
            "jonah hill",
            "matthew mcconaughey",
        ],
        "8.2 on IMDB",
        
    
    ),
    (
        "dune",
        "denis villeneuve",
        2021,
        [
            "timothee chalamet",
            "oscar issac",
            "zendaya",
            "jason momoa",
        ],
        "8 on IMDB",

    ),
    (
        "the nightmare before christmas",
        "henry selick",
        1993,
        [
            "danny elfman",
            "chris sarandon",
            "william hickey",
            "ken page",
        ],
        "7.9 on IMDB",

    ),
    (
        "john wick: chapter 4",
        "chad stahelski",
        2023,
        [
            "keanu reeves",
            "lawrence fishburne",
            "lance reddick",
            "clancy brown",
            "donnie yen",
        ],
        "7.8 on IMDB",

    ),
    (
    

    ),
    (


    ),
    (


    ),
    (


    ),
    (




    # ),
    # (


    # ),
    # (


    # ),
    # (


    # ),
    # (


    # ),
    # (


    # ),
]
