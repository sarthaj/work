# goibibo-API-client

A Python client for accessing GoIbibo's API - [https://developer.goibibo.com/docs](https://developer.goibibo.com/docs)

#### Usage

You need to get your `APP_ID` and `APP_KEY` from [https://developer.goibibo.com/docs](https://developer.goibibo.com/docs)

    from goibibo import goibiboAPI

    GO = goibiboAPI(YOUR_APP_ID, YOUR_APP_KEY)

    print GO.FlightSearch("BLR", "HYD", 20141028)
    print GO.MinimumFare("BLR", "HYD", 20141028)
    print GO.BusSearch("bangalore", "hyderabad", 20141028)
    print GO.BusSeatMap("vJ52KC0ymd0635qTD9bDDy9GHBkGl5FJMJje0aFX\
                        _GQTyev_4N9Y62TTfrmS-Re3dCHl0-UxLq4AsoQ%3D")
    print GO.SearchHotelsByCity(6771549831164675055)
    print GO.GetHotelData([1017089108070373346, 6085103403340214927])
    print GO.GetHotelPriceByCity(6771549831164675055, 20141101, 20141102)

For detailed description of parameters,
look into goibiboAPI.py's  [documentation](https://github.com/pratapvardhan/goibibo-API-client/blob/master/goibibo.py).
