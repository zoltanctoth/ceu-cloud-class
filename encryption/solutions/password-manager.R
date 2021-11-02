install.packages("digest")
library(digest)

encrypt <- function(s) digest(s, algo="sha256")

init.table <- function(){
  return <- data.frame(user.name=character(),
                       password=character(),
                       stringsAsFactors=FALSE) 
}

add.or.update.user <- function(df, user.name, password){
  df.without.user <- df[df$user.name != user.name,]
  rbind(df.without.user, data.frame(user.name=user.name, password=encrypt(password)))
}

authenticate.user <- function (df, user.name, password){
  nrow(df[(df$user.name == user.name) & (df$password == encrypt(password)),]) == 1
}

user.df <- init.table()
user.df <- add.or.update.user(user.df, "example_user", "example_password")
user.df <- add.or.update.user(user.df, "example_user", "example_password_2")

# These all must be TRUE
print(nrow(user.df[user.df$password == "example_password_2",]) == 0)
print(nrow(user.df[user.df$user.name == "example_user",]) == 1)
print(authenticate.user(user.df, "example_user", "example_password_2"))
print(!authenticate.user(user.df, "example_user", "example_password"))
