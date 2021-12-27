using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class CreaOggetti : MonoBehaviour {

    SCL_PositionalControllerInput controllerInput;
    public GameObject proiettile;
    public int count=0;
    Vector3 vec = new Vector3(0, 0, 0);
    public Vector3 a,b,c;

    void Start()
    {
        GameObject proiettile = Resources.Load<GameObject>("marker");
        controllerInput = gameObject.GetComponent<SCL_PositionalControllerInput>();
    }

    void Update()

    {
        if (controllerInput.GetPositionValue() != vec && transform.position != controllerInput.GetPositionValue())
        {
            if (count == 68)
            {
                GameObject[] arr = GameObject.FindGameObjectsWithTag("marker");

                foreach (GameObject marker in arr)
                    GameObject.Destroy(marker);

                count = 0;
            }

            transform.position = controllerInput.GetPositionValue();
            Instantiate(proiettile, transform.position, transform.rotation);
            count++;
            if (count == 40)
            {
                a = transform.position;
            }
            if (count == 43)
            {
                b = transform.position;
            }
            if (count == 52)
            {
                c = transform.position;
            }

        }


    }

}