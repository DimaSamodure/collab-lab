// Hackuble-style 3D cube generator - miZappa style.
// A hackable C# scripting environment for 3D modeling.
// Generates a cube as OBJ vertices/faces, size is hackable.
// Usage: dotnet run -- 2.5
using System;

class Cube {
  static void Main(string[] args) {
    double s = args.Length > 0 ? double.Parse(args[0]) : 1.0;
    double h = s / 2;
    double[,] v = {
      {-h,-h,-h}, {h,-h,-h}, {h,h,-h}, {-h,h,-h},
      {-h,-h,h}, {h,-h,h}, {h,h,h}, {-h,h,h}
    };
    for (int i = 0; i < 8; i++)
      Console.WriteLine($"v {v[i,0]} {v[i,1]} {v[i,2]}");
    int[,] f = {{1,2,3,4},{5,8,7,6},{1,5,6,2},{2,6,7,3},{3,7,8,4},{5,1,4,8}};
    for (int i = 0; i < 6; i++)
      Console.WriteLine($"f {f[i,0]} {f[i,1]} {f[i,2]} {f[i,3]}");
    Console.WriteLine($"# cube size={s} vertices=8 faces=6");
  }
}
