FROM openjdk
WORKDIR /usr/app
COPY ./pom.xml
COPY ./src ./src
RUN mvn clean package -DskipTests
EXPOSE 8081
CMD ["java", "-jar", "target/*.jar"]