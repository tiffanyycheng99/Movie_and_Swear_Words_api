
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import json
from flask import Flask, jsonify

database_path = 'movieSwears.db'
engine = create_engine(f'sqlite:///{database_path}')
Base = automap_base()
Base.prepare(engine, reflect=True)
movie_swear = Base.classes.movie_swear

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
        return (f"Welcome to the Data of Movies and Swear Words.<br/><br/>"
                "Available Route:<br/>" 
                "/api/v1.0/get_movie_swear<br/>")

@app.route("/api/v1.0/get_movie_swear")
def get_movie_swear():
        session = Session(engine)
        results = session.query(movie_swear.field1, movie_swear.color, movie_swear.director_name, movie_swear.num_critic_for_reviews, movie_swear.duration, movie_swear.director_facebook_likes, movie_swear.actor_3_facebook_likes, movie_swear.actor_2_name, movie_swear.actor_1_facebook_likes, movie_swear.actor_1_name,  movie_swear.title, movie_swear.num_voted_users, movie_swear.cast_total_facebook_likes, movie_swear.actor_3_name,  movie_swear.facenumber_in_poster, movie_swear.plot_keywords, movie_swear.movie_imdb_link, movie_swear.num_user_for_reviews, movie_swear.language, movie_swear.country, movie_swear.content_rating, movie_swear.title_year, movie_swear.actor_2_facebook_likes, movie_swear.imdb_score, movie_swear.aspect_ratio, movie_swear.movie_facebook_likes, movie_swear.Action, movie_swear.Adventure, movie_swear.Animation, movie_swear.Biography, movie_swear.Comedy, movie_swear.Crime, movie_swear.Documentary, movie_swear.Drama, movie_swear.Family, movie_swear.Fantasy, movie_swear.Film_Noir, movie_swear.Game_Show, movie_swear.History, movie_swear.Horror, movie_swear.Music, movie_swear.Musical, movie_swear.Mystery, movie_swear.News, movie_swear.Reality_TV, movie_swear.Romance, movie_swear.Sci_Fi, movie_swear.Short, movie_swear.Sport, movie_swear.Thriller, movie_swear.War, movie_swear.Western, movie_swear.breakeven, movie_swear.gross_inmillionsUSD, movie_swear.budget_inmillionsUSD, movie_swear.profit_inmillionsUSD, movie_swear.Swear_Count, movie_swear.Fuck_Count, movie_swear.Shit_Count, movie_swear.Bitch_Count, movie_swear.Cunt_Count, movie_swear.Profanity).all()
        movie_data = []

        for field1, color, director_name, num_critic_for_reviews, duration, director_facebook_likes, actor_3_facebook_likes, actor_2_name, actor_1_facebook_likes, actor_1_name, title, num_voted_users, cast_total_facebook_likes, actor_3_name, facenumber_in_poster, plot_keywords, movie_imdb_link, num_user_for_reviews, language, country, content_rating, title_year, actor_2_facebook_likes, imdb_score, aspect_ratio, movie_facebook_likes, Action, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, Film_Noir, Game_Show, History, Horror, Music, Musical, Mystery, News, Reality_TV, Romance, Sci_Fi, Short, Sport, Thriller, War, Western, breakeven, gross_inmillionsUSD, budget_inmillionsUSD, profit_inmillionsUSD, Swear_Count, Fuck_Count, Shit_Count, Bitch_Count, Cunt_Count, Profanity, in results:
                movie_dict = {}
                movie_dict["field1"] = field1
                movie_dict["color"] = color
                movie_dict["director_name"] = director_name
                movie_dict["num_critic_for_reviews"] = num_critic_for_reviews
                movie_dict["duration"] = duration
                movie_dict["director_facebook_likes"] = director_facebook_likes
                movie_dict["actor_3_facebook_likes"] = actor_3_facebook_likes
                movie_dict["actor_2_name"] = actor_2_name
                movie_dict["actor_1_facebook_likes"] = actor_1_facebook_likes
                movie_dict["actor_1_name"] = actor_1_name
                movie_dict["title"] = title
                movie_dict["num_voted_users"] = num_voted_users
                movie_dict["cast_total_facebook_likes"] = cast_total_facebook_likes
                movie_dict["actor_3_name"] = actor_3_name
                movie_dict["facenumber_in_poster"] = facenumber_in_poster
                movie_dict["plot_keywords"] = plot_keywords
                movie_dict["movie_imdb_link"] = movie_imdb_link
                movie_dict["num_user_for_reviews"] = num_user_for_reviews
                movie_dict["language"] = language
                movie_dict["country"] = country
                movie_dict["content_rating"] = content_rating
                movie_dict["title_year"] = title_year
                movie_dict["actor_2_facebook_likes"] = actor_2_facebook_likes
                movie_dict["imdb_score"] = imdb_score
                movie_dict["aspect_ratio"] = aspect_ratio
                movie_dict["movie_facebook_likes"] = movie_facebook_likes
                movie_dict["Action"] = Action
                movie_dict["Adventure"] = Adventure
                movie_dict["Animation"] = Animation
                movie_dict["Biography"] = Biography
                movie_dict["Comedy"] = Comedy
                movie_dict["Crime"] = Crime
                movie_dict["Documentary"] = Documentary
                movie_dict["Drama"] = Drama
                movie_dict["Family"] = Family
                movie_dict["Fantasy"] = Fantasy
                movie_dict["Film_Noir"] = Film_Noir
                movie_dict["Game_Show"] = Game_Show
                movie_dict["History"] = History
                movie_dict["Horror"] = Horror
                movie_dict["Music"] = Music
                movie_dict["Musical"] = Musical
                movie_dict["Mystery"] = Mystery
                movie_dict["News"] = News
                movie_dict["Reality_TV"] = Reality_TV
                movie_dict["Romance"] = Romance
                movie_dict["Sci_Fi"] = Sci_Fi
                movie_dict["Short"] = Short
                movie_dict["Sport"] = Sport
                movie_dict["Thriller"] = Thriller
                movie_dict["War"] = War
                movie_dict["Western"] = Western
                movie_dict["breakeven"] = breakeven
                movie_dict["gross_inmillionsUSD"] = gross_inmillionsUSD
                movie_dict["budget_inmillionsUSD"] = budget_inmillionsUSD
                movie_dict["profit_inmillionsUSD"] = profit_inmillionsUSD
                movie_dict["Swear_Count"] = Swear_Count
                movie_dict["Fuck_Count"] = Fuck_Count,
                movie_dict["Shit_Count"] = Shit_Count
                movie_dict["Bitch_Count"] = Bitch_Count
                movie_dict["Cunt_Count"] = Cunt_Count
                movie_dict["Profanity"] = Profanity
                movie_data.append(movie_dict)

        # results = session.execute("SELECT * FROM movie_swear")
        #response = [dict(row.items()) for row in results]
     #   all_results = json.dumps(response)

        return(jsonify(movie_data))

        session.close()
 #       movie_swear_json = all_results
  #      return(movie_swear_json)

if __name__ == '__main__':
    app.run(debug=True)