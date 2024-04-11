# Build
FROM node:20-alpine as build
ENV NODE_ENV production
WORKDIR /app
COPY public/ /public
COPY src/ /src
COPY package.json /
RUN npm install
COPY . .
RUN npm run build

# Deploy
FROM nginx:1.25.2-alpine as production
ENV NODE_ENV=production
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=build /app/build .
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
