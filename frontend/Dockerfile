# Build phase
FROM node:20-alpine as builder
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Serve phase
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html

# # Build stage
# FROM node:20 as builder

# WORKDIR /app
# COPY . .
# RUN npm install
# RUN npm run build

# # Production stage
# FROM nginx:alpine
# COPY --from=builder /app/dist /usr/share/nginx/html
# EXPOSE 80

