# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install any needed packages
RUN npm install

# Bundle app source inside Docker image
COPY . .

# Build the app for production
RUN npm run build

# Install `serve` to run the application
RUN npm install -g serve

# Command to run the app
CMD ["serve", "-s", "build", "-l", "5000"]

# Expose port 5000
EXPOSE 5000