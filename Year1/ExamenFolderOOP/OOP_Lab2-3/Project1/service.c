#include <string.h>
#include "service.h"

bool check_if_valid_continent(char continent[]) {
    ///Function to check if the continent is valid
    ///\param continent - the name of the continent
    ///\return - true if it is valid, false otherwise
    const char* Continents[] = { "Europe", "Asia", "America", "Africa", "Australia" };
    int index = 0;
    bool valid = false;
    while (index < sizeof(Continents) / sizeof(const char*) && valid == false) {
        if (strcmp(continent, Continents[index]) == 0)
            valid = true;
        index++;
    }
    return valid;
}

int add_country(Repository* country_list, UndoRedoRepository* undo_redo_repo, char name[], char continent[], unsigned long int population) {
    ///ADD functionality
    ///Service function to create the new element and pass it to be added to the list.
    /// \param country_list - the repository in which the elements are stored
    /// \param undo_redo_repo - the undo and redo repository, for the undo redo functionalities
    /// \param name - name of the country
    /// \param continent - name of the continent, one from Europe, Asia, America, Africa or Australia
    /// \param population - the number of people from the country, stored in millions
    /// \return - 1 if the country already exists, 2 if the continent is not valid, 0 if the couuntry was added successfully
    int index;
    for (index = 0; index < country_list->dynamicArray.length; index++) {
        if (strcmp(getName(&country_list->dynamicArray.data[index]), name) == 0) // check if we already have the country
            return 1;
    }
    if (check_if_valid_continent(continent) == false) // check if the continent is valid
        return 2;
    Country new_country = createCountry(name, continent, population); // create the element
    addUndoElement(undo_redo_repo, country_list); // pass the current repo to the undo repo
    addCountry(country_list, new_country);
    return 0;
}

bool delete_country(Repository* country_list, UndoRedoRepository* undo_redo_repo, char name[]) {
    /// DELETE functionality
    /// Service function to identify and delete the required element given by the user.
    /// \param country_list - the repository in which the elements are stored
    /// \param undo_redo_repo - the undo and redo repository, for the undo redo functionalities
    /// \param name - name of the country to be deleted
    /// \return - false if the element does not exist, true if it exist and it was deleted
    int deleted_index = findByName(country_list, name); // find the index of the element to be deleted
    if (deleted_index == -1)
        return false;
    else {
        addUndoElement(undo_redo_repo, country_list); // pass the current repo to the undo repo
        deleteCountry(country_list, deleted_index);
        return true;
    }
}

int update_country(Repository* country_list, UndoRedoRepository* undo_redo_repo, char old_name[], char name[], char continent[], unsigned long int new_population) {
    ///UPDATE (first type) functionality
    ///Service function to update the name, continent and/or the population of a specific country.
    /// \param country_list - the repository in which the elements are stored
    /// \param undo_redo_repo - the undo and redo repository, for the undo redo functionalities
    /// \param old_name - the name of the country to be updated
    /// \param new_name - the new name of the country, can be the same as the old one
    /// \param continent - the new name of the continent, can be the same as the old one
    /// \param population - the new number of people in the country, can be the same as the old one
    /// \return - 2 if the continent is not valid, 1 if the country to be updated does not exist, 0 if it exists and it was updated
    if (check_if_valid_continent(continent) == false) // check if the continent is valid
        return 2;
    int update_index = findByName(country_list, old_name); // find the index of the element to be updated
    if (update_index == -1)
        return 1;
    Country updated_country = createCountry(name, continent, new_population); // create the new element
    addUndoElement(undo_redo_repo, country_list); // pass the current repo to the undo repo
    updateCountry(country_list, update_index, updated_country);
    return 0;
}

int migration(Repository* country_list, UndoRedoRepository* undo_redo_repo, char old_name[], char new_name[], unsigned long int migrators) {
    /// UPDATE (second type) functionality
    /// Service function to update the population of two countries through migration.
    /// \param country_list - the repository in which the elements are stored
    /// \param undo_redo_repo - the undo and redo repository, for the undo redo functionalities
    /// \param old_name - the name of the country to be updated
    /// \param new_name - the new name of the country, can be the same as the old one
    /// \param migrators - the number of people that want to migrate
    /// \return - 1 if the old country does not exist, 2 if the new country does not exist, 0 if the population mirated successfully
    int index_of_old_country = findByName(country_list, old_name); // find the index of the old country
    int index_of_new_country = findByName(country_list, new_name); // find the index of the new country
    if (index_of_old_country == -1)
        return 1;
    else if (index_of_new_country == -1)
        return 2;
    else {
        addUndoElement(undo_redo_repo, country_list); // pass the current repo to the undo repo
        migrationUpdate(country_list, index_of_old_country, index_of_new_country, migrators);
        return 0;
    }
}

int filter_country(Repository* country_list, const char filter_string[], Country valid_countries[]) {
    ///Filter functionality
    ///Function to filter by a given string and by names the existent countries
    /// \param country_list - the repository in which the elements are stored
    /// \param filter_string - the string by which the names are filtered
    /// \param valid_countries - the array in which the valid countries will be stored
    /// \return - the number of elements from the valid_countries array
    int counter = 0;
    int index;
    if (filter_string[0] == '\0') // case for when the string is empty
        for (index = 0; index < country_list->dynamicArray.length; index++) {
            strcpy(valid_countries[counter].name, country_list->dynamicArray.data[index].name);
            strcpy(valid_countries[counter].continent, country_list->dynamicArray.data[index].continent);
            valid_countries[counter].population = country_list->dynamicArray.data[index].population; // copy everything in the array[counter]
            counter++; // increase the number of elements from the array
        }
    else {
        for (index = 0; index < country_list->dynamicArray.length; index++) {
            if (strstr(country_list->dynamicArray.data[index].name, filter_string) != NULL) { // if the string can be found in the name, copy in array[counter]
                strcpy(valid_countries[counter].name, country_list->dynamicArray.data[index].name);
                strcpy(valid_countries[counter].continent, country_list->dynamicArray.data[index].continent);
                valid_countries[counter].population = country_list->dynamicArray.data[index].population;
                counter++; // increase the number of elements from the array
            }
        }
    }
    return counter;
}

int filter_sort_continent(Repository* country_list, Country valid_countries[], char continent_input[], unsigned long int population) {
    ///Filter and sort functionality
    ///Function to find the countries on a given continent that have a population greater than the given population
    /// \param country_list - the repository in which the elements are stored
    /// \param valid_countries - the array of valid countries
    /// \param continent_input - the name of the continent to filter by
    /// \param population - the number for population comparison
    /// \return - -1 if the continent is not empty or valid, the number of elements from the valid_countries array otherwise
    int counter = 0;
    int index;
    if (continent_input[0] == '\0') { // case if the continent input is empty
        for (index = 0; index < country_list->dynamicArray.length; index++)
            if (country_list->dynamicArray.data[index].population > population) {
                strcpy(valid_countries[counter].name, country_list->dynamicArray.data[index].name);
                strcpy(valid_countries[counter].continent, country_list->dynamicArray.data[index].continent);
                valid_countries[counter].population = country_list->dynamicArray.data[index].population;
                counter++; // copy the elements and increase the counter
            }
    }
    else if (check_if_valid_continent(continent_input) == false) // check if the continent is valid
        return -1;
    else {
        for (index = 0; index < country_list->dynamicArray.length; index++)
            if (strcmp(country_list->dynamicArray.data[index].continent, continent_input) == 0) // if the continent is the same, copy the element and increase the counter
                if (country_list->dynamicArray.data[index].population > population) {
                    strcpy(valid_countries[counter].name, country_list->dynamicArray.data[index].name);
                    strcpy(valid_countries[counter].continent, country_list->dynamicArray.data[index].continent);
                    valid_countries[counter].population = country_list->dynamicArray.data[index].population;
                    counter++;
                }
    }
    // Bubble sort to sort the elements of the array in ascending order
    Country temp; // temporary variable for swapping the elements
    for (int i = 0; i < counter - 1; i++)
        // Last i elements are already in place
        for (int j = 0; j < counter - i - 1; j++)
            if (valid_countries[j].population > valid_countries[j + 1].population) { // if the elements correspond, do the swapping
                temp = valid_countries[j];
                valid_countries[j] = valid_countries[j + 1];
                valid_countries[j + 1] = temp;
            }
    return counter;
}

int ServiceUndo(Repository* country_list, UndoRedoRepository* undo_redo_repo) {
    ///UNDO service function
    ///Function to undo the last operation done
    /// \param country_list - the repository in which the elements are stored
    /// \param undo_redo_repo - the undo and redo repository
    /// \return - 1 if there are no more operations to be undone, 0 otherwise
    if (undo_redo_repo->length_undo == 0)
        return 1;
    addRedoElement(undo_redo_repo, country_list); // add the current repo for the redo operation
    popLastUndo(undo_redo_repo, country_list);
    return 0;
}

int ServiceRedo(Repository* country_list, UndoRedoRepository* undo_redo_repo) {
    ///REDO service function
    ///Function to redo the last operation done
    /// \param country_list - the repository in which the elements are stored
    /// \param undo_redo_repo - the undo and redo repository
    /// \return - 1 if there are no more operations to be redone, 0 otherwise
    if (undo_redo_repo->length_redo == 0)
        return 1;
    addUndoElement(undo_redo_repo, country_list); // add the current repo for the undo operation
    popLastRedo(undo_redo_repo, country_list);
    return 0;
}

























<!DOCTYPE html>
<html>
<head>
<title>Body Building< / title>
< / head>
<body>
<header>
<article>
<h1>Body Building< / h1>
<p>Bodybuilding is the use of progressive resistance exercise to control and develop one's muscles (muscle building) by muscle hypertrophy for aesthetic purposes. To wikipedia please visit: <a href="https://en.wikipedia.org/wiki/Bodybuilding">https://en.wikipedia.org/wiki/Bodybuilding</a></p>
< / article >
<hr / >
<nav>
<h3>Links to Video and Sound of BodyBuilders< / h3>
<ul>
<li><a href = "#BodyBuilder-video">BodyBuilders Video< / a>< / li>
<li><a href = "#BodyBuilder-sound">BodyBuilders Sound< / a>< / li>
< / ul>
< / nav>
< / header>
<main>
<div>
<section id = "BodyBuilder-video">
<h4>BoduBuilder Video< / h4>
<figure>
<video width = "200" controls>
<source src = "videoRoonie.mp4" type = "video/mp4">
Your browser does not support the video tag.
< / video>
<br / ><figurecaption>Roonie Coleman Squatting Video< / figurecaption>
< / figure>
< / section>
< / div>
<div>
<section id = "BodyBuilder-sound">
<h4>BodyBuilder Sound< / h4>
<figure>
<audio controls autoplay>
<source src = "audioRonnie.ogg" type = "audio/ogg">
<source src = "audioRonnie.mp3" type = "audio/mpeg">
Your browser does not support the audio element.
< / audio>
<br / ><figurecaption>Roonie Coleman Sound< / figurecaption>
< / figure>
< / section>
< / div>
<hr / >
<h3>Post - Workout Nutrition< / h3>
<ul>
<li><b>Protein:< / b> Chicken breast, salmon, eggs, Greek yogurt, cottage cheese< / li>
<li><b>Carbohydrates : < / b> Sweet potatoes, brown rice, quinoa, fruits, vegetables< / li>
<li><b>Fats : < / b> Avocado, nuts, nut butter, olive oil, coconut oil< / li>
<li><b>Hydration : < / b> Water, coconut water, sports drinks< / li>
< / ul>
<hr / >
<h3>The table of Supplements with their benefits and photos< / h3>
<table>
<tr>
<th>Suplement    < / th>
<th>Benefits< / th>
<th>Picture< / th>
< / tr>
<tr>
<th>Whey Protein< / th>
<th>Builds and repairs muscle< / th>
<th><img src = "WheyProtein.jpg" alt = "Whey Protein" width = "50" / >< / th>
< / tr>
<tr>
<th>Creatine< / th>
<th>Increases strength and endurance< / th>
<th><img src = "Creatine.jpg" alt = "Creatine" width = "50" / >< / th>
< / tr>
<tr>
<th>BCAAs< / th>
<th>Reduces muscle breakdown< / th>
<th><img src = "BCAA.jpg" alt = "BCAA" width = "100" / >< / th>
< / tr>
< / table>
<hr / >
<aside>
<h3><a href = "https://ro.wikipedia.org/wiki/Ronnie_Coleman">Ronnie Coleman< / a>< / h3>
<p>Ronald "Ronnie" Dean Coleman(born May 13, 1964) is an American retired professional bodybuilder.The winner of the Mr.Olympia title for eight consecutive years, he is widely regarded as either the greatest bodybuilder of all time.< / p>
<img src = "Ronnie_Coleman_Invited_Guest.jpg" alt = "Roonie Coleman" width = "80">
< / aside>
< / main>
<hr / >
<footer>
<svg xmlns = "http://www.w3.org/2000/svg" viewBox = "0 0 200 200" width = "100" height = "80">
<path d = "M28.9 55.9c-10.8 7.5-11.5 22.5-4 33.3 2.9 4.2 6.5 7.7 10.5 10.5 3.3 2.3 6.9 3.9 10.6 5.2-3.6-1.6-6.9-3.6-10.1-6.1-8.6-6.1-15.6-14.6-19.6-24.6zm109.6-13.9c-4 10-11 18.4-19.6 24.5-3.2 2.4-6.5 4.5-10.1 6.1-3.7-1.3-7.3-2.9-10.6-5.2-4-2.8-7.5-6.3-10.5-10.5 7.5-10.9 6.8-25.8-3.9-33.4-8.7-5.9-20.7-5.2-28.4 1.4-4.7 4.2-8.1 9.4-10.4 15.1-3.3 7.3-4.7 15.1-4.1 23.2.9 9.9 4.9 18.7 11.5 26.2 6.5 7.5 14.8 13.1 24.5 16.5 8.4 2.9 17.4 3.7 26.3 2.3 14.3-2.2 26.8-9.7 36.1-20.7 8.8-10.7 14.2-23.7 15.8-37.7 1.1-9.7.6-19.6-1.2-29.3-1.8-8.6-4.6-16.9-8.1-24.9z" / >
< / svg>
<br / >
<p>&copy; 2023 BodyBuilders< / p>
< / footer>
< / body>
< / html>