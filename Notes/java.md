```java
public static String readLine() throws java.io.IndexOutOfBoundsException
{
    byte buffer[] = new byte[512];

    int count = System.in.read(buffer);

    System.in.close()

    return (count==-1)?null:new String(buffer,0,count-2)
}
```