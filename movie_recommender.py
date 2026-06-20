
movies = {
    "3 Idiots": ["Comedy", "Drama"],
    "Dangal": ["Sports", "Drama"],
    "PK": ["Comedy", "Drama"],
    "Shershaah": ["Action", "War"],
    "Pathaan": ["Action", "Thriller"],
    "Jawan": ["Action", "Thriller"],
    "K.G.F Chapter 1": ["Action", "Crime"],
    "K.G.F Chapter 2": ["Action", "Crime"],
    "Pushpa": ["Action", "Drama"],
    "Baahubali": ["Action", "Adventure"],
    "RRR": ["Action", "Drama"],
    "Drishyam": ["Thriller", "Crime"],
    "Andhadhun": ["Thriller", "Crime"],
    "Chhichhore": ["Comedy", "Drama"],
    "Taare Zameen Par": ["Drama", "Family"]
}

user_input = input("Enter your favorite genres (comma separated): ")

user_preferences = [genre.strip().title() for genre in user_input.split(",")]

recommendations = []

for movie, genres in movies.items():
    score = 0

    for genre in user_preferences:
        if genre in genres:
            score += 1

    recommendations.append((movie, score))
 
recommendations.sort(key=lambda x: x[1], reverse=True)

print("\nRecommended Movies:\n")

found = False
for movie, score in recommendations:
    if score > 0:
        found = True
        print(f"{movie} - Match Score: {score}")

if not found:
    print("No matching movies found.")