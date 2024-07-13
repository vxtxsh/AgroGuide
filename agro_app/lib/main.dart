import 'package:agro_app/login.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AgroGuide',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSwatch(primarySwatch: Colors.deepPurple),
        // useMaterial3: true, // This property is not needed unless using Flutter Material 3.0
      ),
      home: const MyHomePage(title: 'AgroGuide'),
    );
  }
}

class MyHomePage extends StatelessWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  Widget build(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;
    double screenHeight = MediaQuery.of(context).size.height;

    return Scaffold(
      backgroundColor: Colors.black,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              width: screenWidth * 0.8, // 80% of screen width
              height: screenHeight * 0.25, // 25% of screen height
              decoration: BoxDecoration(
                color: Colors.green,
                borderRadius: BorderRadius.circular(
                    screenWidth * 0.1), // Adjust based on screen width
                image: DecorationImage(
                  image: AssetImage(
                      'assets/images/ines-alvarez-fdez-OTdmEW5HArg-unsplash.jpg'),
                  fit: BoxFit.cover,
                ),
              ),
              child: Center(
                child: Text(
                  'AgroGuide',
                  style: TextStyle(
                    fontSize: screenWidth * 0.1, // Adjust based on screen width
                    fontWeight: FontWeight.w700,
                    color: Colors.white,
                  ),
                ),
              ),
            ), // Spacer
            GestureDetector(
              onTap: () => Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => LoginPage(),
                ),
              ),
              child: Material(
                elevation: 10,
                borderRadius: BorderRadius.circular(30),
                clipBehavior: Clip.hardEdge,
                child: Container(
                  width: screenWidth * 0.9, // 90% of screen width
                  height: screenHeight * 0.6, // 50% of screen height
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(30),
                    image: DecorationImage(
                      image: AssetImage('assets/images/Add a heading.gif'),
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
