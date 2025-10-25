FROM node:18-alpine

WORKDIR /app

RUN npm install -g expo-cli

COPY package*.json ./

RUN npm install

# Install web dependencies
RUN npx expo install react-native-web@~0.19.6 react-dom@18.2.0 @expo/webpack-config@^19.0.0

COPY . .

EXPOSE 19000 19001 19002

# Start Expo development server (Expo Go)
CMD ["npx", "expo", "start", "--tunnel"]
