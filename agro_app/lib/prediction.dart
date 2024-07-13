import 'package:agro_app/homepage.dart';
import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

class prediction extends StatelessWidget {
  const prediction({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.of(context).push(
              MaterialPageRoute(
                builder: (context) => HomePage(),
              ),
            );
          },
        ),
        title: Text(
          'Predict',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: const Color.fromARGB(255, 58, 57, 57),
        centerTitle: true,
      ),
      body: Column(
        children: [
          Expanded(
            child: WebView(
              initialUrl: 'http://192.168.205.24:5001',
              javascriptMode: JavascriptMode.unrestricted,
              onWebViewCreated: (WebViewController webViewController) {},
              onPageStarted: (String url) {},
              onPageFinished: (String url) {},
              onWebResourceError: (WebResourceError error) {
                print("Web resource error: $error");
              },
            ),
          ),
        ],
      ),
    );
  }
}
