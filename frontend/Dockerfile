# Dockerfile pour ProStory-AI Frontend
# Étape 1 : Base des dépendances
FROM node:20-alpine AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .

# Étape 2 : Développement (serveur de dev Next.js)
FROM base AS development
EXPOSE 3000
CMD ["npm", "run", "dev"]

# Étape 3 : Build pour la production
FROM base AS builder
RUN npm run build

# Étape 4 : Serveur de production (Nginx)
FROM nginx:alpine AS production
COPY --from=builder /app/out /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]
