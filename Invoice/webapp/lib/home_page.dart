import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      // appBar: AppBar(
      //   backgroundColor: Colors.white,
      //   leading: Container(
      //     child:
      //   ),
      //   actions: [
      //     IconButton(onPressed: () {}, icon: Icon(Icons.email)),
      //     IconButton(onPressed: () {}, icon: Icon(Icons.phone)),
      //     IconButton(onPressed: () {}, icon: Icon(Icons.shop)),
      //   ],
      // ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                FlutterLogo(size: 100),
                Container(
                  width: 200,
                  child: Row(
                    children: [
                      IconButton(onPressed: () {}, icon: Icon(Icons.email)),
                      IconButton(onPressed: () {}, icon: Icon(Icons.phone)),
                      IconButton(onPressed: () {}, icon: Icon(Icons.shop)),
                    ],
                  ),
                ),
              ],
            ),
            SizedBox(
              height: 20,
            ),
            Container(
                padding: EdgeInsets.symmetric(horizontal: 150, vertical: 30),
                decoration: BoxDecoration(
                    color: Colors.grey,
                    image: DecorationImage(
                      fit: BoxFit.cover,
                      image: AssetImage('assets/images/1.jpg'),
                    )),
                width: double.infinity,
                height: 400,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Container(
                          width: 150,
                          child: ElevatedButton(
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Icon(Icons.access_alarm),
                                Text('add Alarm')
                              ],
                            ),
                            onPressed: () {},
                          ),
                        ),
                        Container(
                          width: 150,
                          child: ElevatedButton(
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Icon(Icons.access_alarm),
                                Text('add Alarm')
                              ],
                            ),
                            onPressed: () {},
                          ),
                        ),
                        Container(
                          width: 150,
                          child: ElevatedButton(
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Icon(Icons.access_alarm),
                                Text('add Alarm')
                              ],
                            ),
                            onPressed: () {},
                          ),
                        ),
                        Container(
                          width: 150,
                          child: ElevatedButton(
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Icon(Icons.access_alarm),
                                Text('add Alarm')
                              ],
                            ),
                            onPressed: () {},
                          ),
                        ),
                        Container(
                          width: 150,
                          child: ElevatedButton(
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Icon(Icons.access_alarm),
                                Text('add Alarm')
                              ],
                            ),
                            onPressed: () {},
                          ),
                        ),
                      ],
                    ),
                    // SizedBox(
                    //   height: 20,
                    // ),
                    // Row(
                    //   mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //   children: [
                    //     Container(
                    //       width: 150,
                    //       child: ElevatedButton(
                    //         child: Row(
                    //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //           children: [
                    //             Icon(Icons.access_alarm),
                    //             Text('add Alarm')
                    //           ],
                    //         ),
                    //         onPressed: () {},
                    //       ),
                    //     ),
                    //     Container(
                    //       width: 150,
                    //       child: ElevatedButton(
                    //         child: Row(
                    //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //           children: [
                    //             Icon(Icons.access_alarm),
                    //             Text('add Alarm')
                    //           ],
                    //         ),
                    //         onPressed: () {},
                    //       ),
                    //     ),
                    //     Container(
                    //       width: 150,
                    //       child: ElevatedButton(
                    //         child: Row(
                    //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //           children: [
                    //             Icon(Icons.access_alarm),
                    //             Text('add Alarm')
                    //           ],
                    //         ),
                    //         onPressed: () {},
                    //       ),
                    //     ),
                    //     Container(
                    //       width: 150,
                    //       child: ElevatedButton(
                    //         child: Row(
                    //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //           children: [
                    //             Icon(Icons.access_alarm),
                    //             Text('add Alarm')
                    //           ],
                    //         ),
                    //         onPressed: () {},
                    //       ),
                    //     ),
                    //     Container(
                    //       width: 150,
                    //       child: ElevatedButton(
                    //         child: Row(
                    //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //           children: [
                    //             Icon(Icons.access_alarm),
                    //             Text('add Alarm')
                    //           ],
                    //         ),
                    //         onPressed: () {},
                    //       ),
                    //     ),
                    //   ],
                    // ),
                    // SizedBox(
                    //   height: 20,
                    // ),
                    // Row(
                    //   mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //   children: [
                    //     Container(
                    //       width: 150,
                    //       child: ElevatedButton(
                    //         child: Row(
                    //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //           children: [
                    //             Icon(Icons.access_alarm),
                    //             Text('add Alarm')
                    //           ],
                    //         ),
                    //         onPressed: () {},
                    //       ),
                    //     ),
                    //     Container(
                    //       width: 150,
                    //       child: ElevatedButton(
                    //         child: Row(
                    //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //           children: [
                    //             Icon(Icons.access_alarm),
                    //             Text('add Alarm')
                    //           ],
                    //         ),
                    //         onPressed: () {},
                    //       ),
                    //     ),
                    //     Container(
                    //       width: 150,
                    //       child: ElevatedButton(
                    //         child: Row(
                    //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //           children: [
                    //             Icon(Icons.access_alarm),
                    //             Text('add Alarm')
                    //           ],
                    //         ),
                    //         onPressed: () {},
                    //       ),
                    //     ),
                    //     Container(
                    //       width: 150,
                    //       child: ElevatedButton(
                    //         child: Row(
                    //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //           children: [
                    //             Icon(Icons.access_alarm),
                    //             Text('add Alarm')
                    //           ],
                    //         ),
                    //         onPressed: () {},
                    //       ),
                    //     ),
                    //     Container(
                    //       width: 150,
                    //       child: ElevatedButton(
                    //         child: Row(
                    //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    //           children: [
                    //             Icon(Icons.access_alarm),
                    //             Text('add Alarm')
                    //           ],
                    //         ),
                    //         onPressed: () {},
                    //       ),
                    //     ),
                    //   ],
                    // ),
                    // // SizedBox(
                    // //   height: 20,
                    // // ),
                    // // Row(
                    // //   mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //   children: [
                    // //     Container(
                    // //       width: 150,
                    // //       child: ElevatedButton(
                    // //         child: Row(
                    // //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //           children: [
                    // //             Icon(Icons.access_alarm),
                    // //             Text('add Alarm')
                    // //           ],
                    // //         ),
                    // //         onPressed: () {},
                    // //       ),
                    // //     ),
                    // //     Container(
                    // //       width: 150,
                    // //       child: ElevatedButton(
                    // //         child: Row(
                    // //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //           children: [
                    // //             Icon(Icons.access_alarm),
                    // //             Text('add Alarm')
                    // //           ],
                    // //         ),
                    // //         onPressed: () {},
                    // //       ),
                    // //     ),
                    // //     Container(
                    // //       width: 150,
                    // //       child: ElevatedButton(
                    // //         child: Row(
                    // //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //           children: [
                    // //             Icon(Icons.access_alarm),
                    // //             Text('add Alarm')
                    // //           ],
                    // //         ),
                    // //         onPressed: () {},
                    // //       ),
                    // //     ),
                    // //     Container(
                    // //       width: 150,
                    // //       child: ElevatedButton(
                    // //         child: Row(
                    // //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //           children: [
                    // //             Icon(Icons.access_alarm),
                    // //             Text('add Alarm')
                    // //           ],
                    // //         ),
                    // //         onPressed: () {},
                    // //       ),
                    // //     ),
                    // //     Container(
                    // //       width: 150,
                    // //       child: ElevatedButton(
                    // //         child: Row(
                    // //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //           children: [
                    // //             Icon(Icons.access_alarm),
                    // //             Text('add Alarm')
                    // //           ],
                    // //         ),
                    // //         onPressed: () {},
                    // //       ),
                    // //     ),
                    // //   ],
                    // // ),
                    // // SizedBox(
                    // //   height: 20,
                    // // ),
                    // // Row(
                    // //   mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //   children: [
                    // //     Container(
                    // //       width: 150,
                    // //       child: ElevatedButton(
                    // //         child: Row(
                    // //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //           children: [
                    // //             Icon(Icons.access_alarm),
                    // //             Text('add Alarm')
                    // //           ],
                    // //         ),
                    // //         onPressed: () {},
                    // //       ),
                    // //     ),
                    // //     Container(
                    // //       width: 150,
                    // //       child: ElevatedButton(
                    // //         child: Row(
                    // //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //           children: [
                    // //             Icon(Icons.access_alarm),
                    // //             Text('add Alarm')
                    // //           ],
                    // //         ),
                    // //         onPressed: () {},
                    // //       ),
                    // //     ),
                    // //     Container(
                    // //       width: 150,
                    // //       child: ElevatedButton(
                    // //         child: Row(
                    // //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //           children: [
                    // //             Icon(Icons.access_alarm),
                    // //             Text('add Alarm')
                    // //           ],
                    // //         ),
                    // //         onPressed: () {},
                    // //       ),
                    // //     ),
                    // //     Container(
                    // //       width: 150,
                    // //       child: ElevatedButton(
                    // //         child: Row(
                    // //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //           children: [
                    // //             Icon(Icons.access_alarm),
                    // //             Text('add Alarm')
                    // //           ],
                    // //         ),
                    // //         onPressed: () {},
                    // //       ),
                    // //     ),
                    // //     Container(
                    // //       width: 150,
                    // //       child: ElevatedButton(
                    // //         child: Row(
                    // //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    // //           children: [
                    // //             Icon(Icons.access_alarm),
                    // //             Text('add Alarm')
                    // //           ],
                    // //         ),
                    // //         onPressed: () {},
                    // //       ),
                    // //     ),
                    // //   ],
                    // // ),
                  ],
                )
                // Center(
                //   child: Wrap(
                //     // gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                //     //   crossAxisCount: 5,
                //     // ),
                //     // crossAxisAlignment: C,
                //     spacing: 20.0,
                //     runSpacing: 20,
                //     children: [
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //       Container(
                //         color: Colors.green,
                //         width: 100,
                //         height: 50,
                //       ),
                //     ],
                //   ),
                // ),
                ),
            SizedBox(
              height: 20,
            ),
            Container(
              height: 300,
              child: Align(
                alignment: Alignment.topCenter,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    Container(
                      width: 100,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Icon(Icons.facebook),
                          Text('Facebook'),
                        ],
                      ),
                    ),
                    Container(
                      width: 120,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Icon(Icons.contacts),
                          Text('Contact Us'),
                        ],
                      ),
                    ),
                    Container(
                      width: 120,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          FlutterLogo(),
                          Text('Contact Us'),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
