data_old <- read.table("data.csv", header=T,sep=",",dec=".")
data_old

colnames(data_old)[1]  <- "generation"
colnames(data_old)[2]  <- "prey_1"
colnames(data_old)[3]  <- "prey_2"
colnames(data_old)[4]  <- "predator"

str(data_old)
head(data_old)

plot(data_old)

library(ggplot2)
library(tidyverse)

data_new <- data_old %>% pivot_longer(prey_1:predator, names_to = "species", values_to = "population")
data_new <- as.data.frame(data_new)
head(data_new)
str(data_new)

ggplot(data = data_new, aes(x = generation , y = population)) + 
  geom_line(aes(color = species)) + 
  scale_color_brewer(NULL, palette = "Set1") + theme_minimal() +
  labs(title = "Lotka-Volterra Predator Prey Model", x = "# of generations", y = "Population density")

plot(data_old$prey_1, data_old$predator, type="l", col="blue")
lines(data_old$prey_2, data_old$predator, col="orange")

     