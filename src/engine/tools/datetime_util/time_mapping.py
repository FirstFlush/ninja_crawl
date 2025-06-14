from ..base import BaseSubstringMapping


class TimeMapping(BaseSubstringMapping):

    CLOCK_TIMES = {
        # 12-hour clock time mappings (every 15 minutes)
        "12:00": {"1200", "twelve", "twelveoclock",},
        "12:15": {"1215", "twelvefifteen"},
        "12:30": {"1230", "twelvethirty"},
        "12:45": {"1245", "twelvefortyfive", "twelvefourtyfive"},
        
        "1:00": {"0100", "one", "oneoclock"},
        "1:15": {"0115", "onefifteen"},
        "1:30": {"0130", "onethirty"},
        "1:45": {"0145", "onefortyfive", "onefourtyfive"},
        
        "2:00": {"0200", "two", "twooclock"},
        "2:15": {"0215", "twofifteen"},
        "2:30": {"0230", "twothirty"},
        "2:45": {"0245", "twofortyfive", "twofourtyfive"},
        
        "3:00": {"0300", "three", "threeoclock"},
        "3:15": {"0315", "threefifteen"},
        "3:30": {"0330", "threethirty"},
        "3:45": {"0345", "threefortyfive", "threefourtyfive"},
        
        "4:00": {"0400", "four", "fouroclock"},
        "4:15": {"0415", "fourfifteen"},
        "4:30": {"0430", "fourthirty"},
        "4:45": {"0445", "fourfortyfive", "fourfourtyfive"},
        
        "5:00": {"0500", "five", "fiveoclock"},
        "5:15": {"0515", "fivefifteen"},
        "5:30": {"0530", "fivethirty"},
        "5:45": {"0545", "fivefortyfive", "fivefourtyfive"},
        
        "6:00": {"0600", "six", "sixoclock"},
        "6:15": {"0615", "sixfifteen"},
        "6:30": {"0630", "sixthirty"},
        "6:45": {"0645", "sixfortyfive", "sixfourtyfive"},
        
        "7:00": {"0700", "seven", "sevenoclock"},
        "7:15": {"0715", "sevenfifteen"},
        "7:30": {"0730", "seventhirty"},
        "7:45": {"0745", "sevenfortyfive", "sevenfourtyfive"},
        
        "8:00": {"0800", "eight", "eightoclock"},
        "8:15": {"0815", "eightfifteen"},
        "8:30": {"0830", "eightthirty"},
        "8:45": {"0845", "eightfortyfive", "eightfourtyfive"},
        
        "9:00": {"0900", "nine", "nineoclock"},
        "9:15": {"0915", "ninefifteen"},
        "9:30": {"0930", "ninethirty"},
        "9:45": {"0945", "ninefortyfive", "ninefourtyfive"},
        
        "10:00": {"1000", "ten", "tenoclock"},
        "10:15": {"1015", "tenfifteen"},
        "10:30": {"1030", "tenthirty"},
        "10:45": {"1045", "tenfortyfive", "tenfourtyfive"},
        
        "11:00": {"1100", "eleven", "elevenoclock"},
        "11:15": {"1115", "elevenfifteen"},
        "11:30": {"1130", "eleventhirty"},
        "11:45": {"1145", "elevenfortyfive", "elevenfourtyfive"}
    }

    KEYWORDS = {
        "12:00am": {"midnight"},
        "12:00pm": {"noon"},
    }

    TIME_CONTEXTS = {
        "am": {
            "morning", "breakfast", "brightandearly", "sunrise", "dawn", "beforelunch", "beforenoon", "aftermidnight",
        },
        "pm": {
            "dinner", "evening", "afternoon", "afterlunch", "night", "sunset", "dusk" "supper", 
            "afterhours", "endofday", "beforemidnight",
        },
    }
