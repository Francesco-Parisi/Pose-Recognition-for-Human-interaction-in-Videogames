
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraScript : MonoBehaviour
{
    public Camera cam;
    private Vector3 previousPosition;

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(1))
        {
            previousPosition = cam.ScreenToViewportPoint(Input.mousePosition);
        }

        if (Input.GetMouseButton(1))
        {
            Vector3 direction = previousPosition - cam.ScreenToViewportPoint(Input.mousePosition);

            //cam.transform.RotateAround(new Vector3(),new Vector3(1,0,0), direction.y * 180);
            cam.transform.RotateAround(new Vector3(), new Vector3(0, 1, 0), -direction.x * 180);

            previousPosition = cam.ScreenToViewportPoint(Input.mousePosition);
        }

    }
}