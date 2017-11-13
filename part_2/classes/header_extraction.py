#You may have noticed when printing the data that the first element in the list of rows contains some header information.
#Using the csv module, we don't have a way of extracting this header unless we grab the first element.
#However, with our dataset class, we could add an instance method that would grab the first result of self.data,
#set it as a header attribute, and then remove it from the data attribute.
