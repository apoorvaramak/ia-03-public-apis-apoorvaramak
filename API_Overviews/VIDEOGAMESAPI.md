URL: https://rawg.io/apidocs

This API is a database of video games, including the names of the games, genres, platforms, stores, publishers, and more. Rawg requires a key, but it is free to have up to 20,000 requests a month on the free plan once you make an account. On the API documentation site they have many examples of what you can use Rawg to do, like creating bots for apps like discord. There is a lot of games avaiable and many requests allowed on the free version, so this API is very useful for any hobby projects involving video games.

Example Endpoints:
    /games:
        - This endpoint returns all the games that fit a certain criteria depending on which query parameters you use. 
        - There are tons of parameters available that makes searching precisely much more doable such as including platforms, stores, publishers, dates, and more. 
        - If you know what you are not looking for, there's also parameters that allow you to exclude certain platforms, stores, and game series.
        - There is also a search query that you can use to find a specific game by it's title.
        - Each of the games have an ID that is returned that can be used to get even more information on the game.
        - The information is returned in a json that has a count of how many results there are and the results array. Converting it to json with .json() and getting the result array from that yields the dictionary of values and some other dictionaries (such as esrb rating and platforms)
        - It also provides a link to the previous and next games in the library, but those responses are not required so the user doesn't need to include those. 

    /games/{id}/achievements:
        - This endpoint gives all of the achievements that a player can earn throughout a certain video games
        - Using the ID that can be retrieved from the above call (/games) users of this API can then find the achievements that are possible in that game.
        - The only parameter it accepts is the ID, and it will return the info about that achievements
        
    /games/{id}/{example-endpoint} 
        - With the game's ID and the many endpoints outlined in the documentation there is a lot of information available.
        - Games trailers, visually similar games, screenshots of the games, which stores to buy the games from and more can be found with from just the game's ID.  
