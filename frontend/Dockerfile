# Use an official Node.js image
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN npm install

# Build the React app (optional for production)
# RUN npm run build

# Expose the port React runs on
EXPOSE 3000

# Command to run the React development server
CMD ["npm", "start"]
