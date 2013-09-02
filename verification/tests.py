"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "H",
            "answer": ["1", u"1s¹", "1"],
            "explanation": "First - 1s¹"
        },
        {
            "input": "He",
            "answer": ["2", u"1s²", "2"],
            "explanation": "Second - 1s²"
        },
        {
            "input": "Al",
            "answer": ["13", u"[Ne] 3s² 3p¹", "2 2 222 2 100"],
            "explanation": "Third - 1s² 2s² 2p⁶ 3s² 3p¹"
        },
        {
            "input": "O",
            "answer": ["8", u"[He] 2s² 2p⁴", "2 2 211"],
            "explanation": "Fourth - 1s² 2s² 2p⁴"
        },
        {
            "input": "Li",
            "answer": ["3", u"[He] 2s¹", "2 1"],
            "explanation": "Fifth - 1s² 2s¹"
        },
        {
            "input": "Uuo",
            "answer": [ "118", u"[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁶", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222 2 2222222 22222 222" ],
            "explanation": "Ununoctium"
        },
        {
            "input": "Cr",
            "answer": [ "24", u"[Ar] 3d⁵ 4s¹", "2 2 222 2 222 1 11111" ],
            "explanation": "Chromium"
        },
        {
            "input": "In",
            "answer": [ "49", u"[Kr] 4d¹⁰ 5s² 5p¹", "2 2 222 2 222 2 22222 222 2 22222 100" ],
            "explanation": "Indium"
        },
        {
            "input": "I",
            "answer": [ "53", u"[Kr] 4d¹⁰ 5s² 5p⁵", "2 2 222 2 222 2 22222 222 2 22222 221" ],
            "explanation": "Iodine"
        },
        {
            "input": "Ir",
            "answer": [ "77", u"[Xe] 4f¹⁴ 5d⁷ 6s²", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22111" ],
            "explanation": "Iridium"
        },
        {
            "input": "Tl",
            "answer": [ "81", u"[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 100" ],
            "explanation": "Thallium"
        },
        {
            "input": "Db",
            "answer": [ "105", u"[Rn] 5f¹⁴ 6d³ 7s²", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222 2 2222222 11100" ],
            "explanation": "Dubnium"
        },
        {
            "input": "V",
            "answer": [ "23", u"[Ar] 3d³ 4s²", "2 2 222 2 222 2 11100" ],
            "explanation": "Vanadium"
        },
        {
            "input": "Rn",
            "answer": [ "86", u"[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222" ],
            "explanation": "Radon"
        },
        {
            "input": "Xe",
            "answer": [ "54", u"[Kr] 4d¹⁰ 5s² 5p⁶", "2 2 222 2 222 2 22222 222 2 22222 222" ],
            "explanation": "Radon"
        },
        {
            "input": "Br",
            "answer": [ "35", u"[Ar] 3d¹⁰ 4s² 4p⁵", "2 2 222 2 222 2 22222 221" ],
            "explanation": "Bromine"
        }
    ],
    "Extra": [
        {
            "input": "Na",
            "answer": [ "11", u"[Ne] 3s¹", "2 2 222 1" ],
        },
        {
            "input": "Kr",
            "answer": [ "36", u"[Ar] 3d¹⁰ 4s² 4p⁶", "2 2 222 2 222 2 22222 222" ],
        },
        {
            "input": "K",
            "answer": [ "19", u"[Ar] 4s¹", "2 2 222 2 222 1" ],
        },
        {
            "input": "Cu",
            "answer": [ "29", u"[Ar] 3d¹⁰ 4s¹", "2 2 222 2 222 1 22222" ],
        },
        {
            "input": "Ds",
            "answer": [ "110", u"[Rn] 5f¹⁴ 6d⁸ 7s²", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222 2 2222222 22211" ],
        },
        {
            "input": "Ar",
            "answer": [ "18", u"[Ne] 3s² 3p⁶", "2 2 222 2 222" ],
        },
        {
            "input": "Rb",
            "answer": [ "37", u"[Kr] 5s¹", "2 2 222 2 222 2 22222 222 1" ],
        },
        {
            "input": "Uus",
            "answer": [ "117", u"[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁵", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222 2 2222222 22222 221" ],
        },
        {
            "input": "Cl",
            "answer": [ "17", u"[Ne] 3s² 3p⁵", "2 2 222 2 221" ],
        },
        {
            "input": "Fr",
            "answer": [ "87", u"[Rn] 7s¹", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222 1" ],
        }
    ]
}
