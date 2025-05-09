# K-th element of two Arrays
# https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

from utils import TestRunner


class SolutionBrute:
    def kthElement(self, k, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        arr = []

        i = j = 0
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
        while i < n1:
            arr.append(arr1[i])
            i += 1
        while j < n2:
            arr.append(arr2[j])
            j += 1
        return arr[k - 1]


class SolutionOptimal:
    def kthElement(self, k, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        if n1 > n2:
            return self.kthElement(k, arr2, arr1)

        i, j = max(0, k - n2), min(n1, k)
        while i <= j:
            mid1 = (i + j) // 2
            if mid1 > k:
                j = mid1 - 1
                continue
            mid2 = k - mid1

            l1, l2, r1, r2 = (
                float("-inf"),
                float("-inf"),
                float("inf"),
                float("inf"),
            )

            if mid1 < n1:
                r1 = arr1[mid1]
            if mid2 < n2:
                r2 = arr2[mid2]
            if (mid1 - 1) >= 0:
                l1 = arr1[mid1 - 1]
            if (mid2 - 1) >= 0:
                l2 = arr2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                j = mid1 - 1
            else:
                i = mid1 + 1
        return -1


cases = [
    {
        "input": {"arr1": [2, 3, 6, 7, 9], "arr2": [1, 4, 8, 10], "k": 5},
        "expected": 6,
    },
    {
        "input": {
            "arr1": [1, 2, 3, 6, 7, 9, 9, 10, 10, 10, 11, 12, 13],
            "arr2": [2, 4, 8, 10],
            "k": 1,
        },
        "expected": 1,
    },
    {
        "input": {
            "k": 7,
            "arr1": [100, 112, 256, 349, 770],
            "arr2": [72, 86, 113, 119],
        },
        "expected": 256,
    },
    {
        "input": {
            "k": 2,
            "arr1": [5, 5, 8, 8, 8, 9, 11, 11, 11, 11, 11],
            "arr2": [4, 4, 4, 4, 6, 8, 9, 9, 9, 11, 13],
        },
        "expected": 4,
    },
    {
        "input": {
            "k": 748,
            "arr1": [
                45,
                45,
                46,
                52,
                53,
                58,
                60,
                61,
                66,
                73,
                74,
                75,
                81,
                87,
                88,
                89,
                93,
                97,
                98,
                99,
                105,
                105,
                105,
                107,
                111,
                111,
                114,
                118,
                120,
                120,
                120,
                122,
                126,
                128,
                129,
                133,
                137,
                137,
                141,
                143,
                147,
                150,
                165,
                168,
                169,
                169,
                170,
                178,
                180,
                181,
                184,
                185,
                190,
                191,
                192,
                197,
                198,
                201,
                201,
                201,
                205,
                206,
                207,
                208,
                209,
                209,
                211,
                213,
                217,
                218,
                225,
                232,
                236,
                238,
                238,
                241,
                248,
                249,
                250,
                252,
                252,
                254,
                255,
                255,
                255,
                259,
                261,
                261,
                263,
                275,
                275,
                276,
                278,
                280,
                280,
                281,
                285,
                287,
                289,
                291,
                291,
                293,
                295,
                295,
                298,
                301,
                301,
                301,
                306,
                306,
                307,
                308,
                308,
                313,
                314,
                314,
                315,
                315,
                319,
                320,
                320,
                323,
                325,
                327,
                335,
                340,
                344,
                347,
                348,
                352,
                353,
                353,
                357,
                359,
                361,
                362,
                364,
                364,
                371,
                374,
                374,
                376,
                377,
                381,
                381,
                382,
                383,
                387,
                389,
                389,
                393,
                394,
                396,
                397,
                399,
                404,
                405,
                411,
                411,
                412,
                414,
                414,
                422,
                427,
                434,
                436,
                442,
                445,
                446,
                447,
                450,
                451,
                455,
                463,
                464,
                464,
                465,
                465,
                472,
                481,
                484,
                485,
                485,
                486,
                488,
                488,
                489,
                489,
                491,
                491,
                492,
                492,
                493,
                494,
                496,
                496,
                496,
                496,
                504,
                510,
                514,
                519,
                520,
                524,
                525,
                529,
                533,
                534,
                535,
                540,
                542,
                543,
                544,
                547,
                547,
                549,
                552,
                554,
                554,
                557,
                557,
                559,
                567,
                567,
                569,
                575,
                576,
                579,
                581,
                582,
                585,
                585,
                585,
                585,
                589,
                590,
                610,
                613,
                615,
                617,
                621,
                626,
                627,
                630,
                635,
                638,
                640,
                641,
                648,
                652,
                653,
                657,
                658,
                658,
                660,
                663,
                664,
                666,
                668,
                669,
                670,
                671,
                677,
                680,
                690,
                693,
                698,
                701,
                702,
                703,
                706,
                709,
                711,
                717,
                718,
                718,
                718,
                721,
                722,
                725,
                725,
                728,
                734,
                735,
                735,
                736,
                740,
                742,
                746,
                749,
                752,
                762,
                767,
                768,
                772,
                776,
                777,
                777,
                778,
                783,
                787,
                788,
                788,
                789,
                792,
                793,
                793,
                795,
                795,
                796,
                798,
                803,
                804,
                808,
                811,
                811,
                812,
                814,
                820,
                826,
                830,
                830,
                835,
                836,
                836,
                843,
                844,
                845,
                845,
                845,
                847,
                847,
                849,
                850,
                850,
                853,
                857,
                859,
                862,
                863,
                864,
                864,
                866,
                867,
                872,
                873,
                874,
                875,
                875,
                876,
                876,
                878,
                879,
                879,
                880,
                880,
                881,
                885,
                895,
                896,
                898,
                900,
                908,
                913,
                915,
                915,
                922,
                927,
                928,
                929,
                932,
                933,
                940,
                942,
                942,
                947,
                949,
                950,
                952,
                952,
                953,
                959,
                960,
                967,
                968,
                968,
                974,
                976,
                986,
                991,
                992,
                993,
                1000,
                1006,
                1014,
                1016,
                1024,
                1025,
                1025,
                1028,
                1031,
                1035,
                1036,
                1037,
            ],
            "arr2": [
                40,
                42,
                46,
                47,
                47,
                47,
                53,
                56,
                57,
                59,
                61,
                61,
                63,
                64,
                65,
                67,
                68,
                69,
                69,
                70,
                70,
                75,
                77,
                79,
                83,
                84,
                90,
                91,
                91,
                93,
                95,
                96,
                103,
                104,
                104,
                105,
                106,
                109,
                110,
                111,
                114,
                120,
                120,
                127,
                128,
                131,
                133,
                135,
                137,
                140,
                140,
                141,
                141,
                142,
                145,
                149,
                156,
                156,
                157,
                158,
                163,
                166,
                166,
                169,
                171,
                171,
                174,
                174,
                179,
                179,
                184,
                188,
                189,
                189,
                191,
                192,
                196,
                197,
                204,
                206,
                211,
                212,
                213,
                214,
                214,
                214,
                215,
                216,
                217,
                218,
                221,
                225,
                230,
                231,
                232,
                234,
                236,
                239,
                242,
                244,
                252,
                253,
                255,
                256,
                256,
                257,
                260,
                265,
                267,
                267,
                268,
                269,
                269,
                271,
                272,
                273,
                273,
                275,
                276,
                277,
                280,
                281,
                283,
                285,
                290,
                294,
                307,
                307,
                310,
                311,
                313,
                316,
                317,
                318,
                322,
                324,
                325,
                326,
                333,
                334,
                334,
                337,
                338,
                340,
                342,
                342,
                343,
                347,
                348,
                356,
                358,
                364,
                366,
                367,
                368,
                369,
                370,
                373,
                375,
                376,
                377,
                380,
                381,
                385,
                387,
                388,
                392,
                402,
                403,
                404,
                405,
                406,
                409,
                410,
                410,
                412,
                413,
                413,
                416,
                420,
                420,
                421,
                423,
                426,
                427,
                428,
                428,
                435,
                437,
                442,
                453,
                456,
                459,
                461,
                465,
                467,
                468,
                471,
                472,
                484,
                486,
                494,
                497,
                501,
                504,
                506,
                507,
                510,
                512,
                513,
                516,
                523,
                526,
                526,
                530,
                534,
                538,
                546,
                548,
                548,
                553,
                554,
                558,
                559,
                562,
                563,
                565,
                574,
                575,
                577,
                577,
                578,
                579,
                580,
                581,
                582,
                584,
                587,
                587,
                589,
                592,
                593,
                595,
                597,
                601,
                603,
                606,
                606,
                608,
                610,
                616,
                618,
                621,
                625,
                626,
                627,
                633,
                634,
                636,
                639,
                642,
                647,
                647,
                648,
                649,
                652,
                652,
                653,
                655,
                656,
                661,
                661,
                663,
                663,
                669,
                673,
                676,
                679,
                682,
                682,
                684,
                685,
                690,
                693,
                694,
                699,
                705,
                706,
                714,
                714,
                716,
                718,
                719,
                723,
                729,
                729,
                729,
                731,
                737,
                738,
                739,
                740,
                740,
                740,
                743,
                747,
                751,
                752,
                753,
                755,
                756,
                756,
                757,
                759,
                769,
                770,
                770,
                774,
                777,
                780,
                781,
                782,
                787,
                787,
                788,
                789,
                789,
                789,
                795,
                800,
                804,
                807,
                808,
                809,
                812,
                812,
                813,
                814,
                815,
                821,
                822,
                827,
                829,
                832,
                834,
                835,
                836,
                837,
                838,
                839,
                840,
                841,
                841,
                844,
                844,
                846,
                847,
                851,
                855,
                856,
                860,
                862,
                863,
                864,
                864,
                865,
                870,
                871,
                874,
                879,
                881,
                883,
                885,
                886,
                887,
                887,
                889,
                890,
                891,
                893,
                897,
                901,
                905,
                906,
                908,
                908,
                909,
                916,
                916,
                920,
                921,
                923,
                924,
                926,
                927,
                927,
                930,
                931,
                932,
                933,
                937,
                937,
                938,
                939,
                941,
                948,
                949,
                950,
                954,
                956,
                958,
                960,
                962,
                967,
                971,
                975,
                981,
                982,
                983,
                983,
                984,
                997,
                997,
                998,
                999,
                1000,
                1000,
                1001,
                1006,
                1006,
                1008,
                1010,
                1011,
                1014,
                1016,
                1016,
                1020,
                1022,
                1025,
                1027,
                1029,
                1031,
                1033,
                1036,
                1036,
                1036,
            ],
        },
        "expected": 908,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().kthElement).test(cases)
    TestRunner(SolutionOptimal().kthElement).test(cases)
