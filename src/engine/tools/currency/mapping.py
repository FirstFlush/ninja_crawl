from ..base import BaseSubstringMapping


class CurrencyMapping(BaseSubstringMapping):
        
    FREE_WORDS = {
        0.0 : {"free", "nocost", "gratis", "complimentary"}
    }
    
    CURRENCY_TYPES = {
        "cad": {"cad", "canadian","canadien",},
        "usd": {"usd", "usdollars", "american", "unitedstates",},
        "gbp": {"gbp", "pound", "pounds", "britishpound", "britishpounds", "£"},
        "eur": {"eur", "euro", "euros", "€"},
        "btc": {"btc", "bitcoin", "₿"},
        "eth": {"eth", "ethereum",}   
    }