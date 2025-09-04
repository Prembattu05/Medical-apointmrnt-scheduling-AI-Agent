{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Prembattu05/Medical-apointmrnt-scheduling-AI-Agent/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ijTmlMOKfpvq",
        "outputId": "b807f413-6418-4c3a-9a02-20401e1ad884"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: langchain in /usr/local/lib/python3.12/dist-packages (0.3.27)\n",
            "Collecting langgraph\n",
            "  Downloading langgraph-0.6.6-py3-none-any.whl.metadata (6.8 kB)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (2.2.2)\n",
            "Requirement already satisfied: openpyxl in /usr/local/lib/python3.12/dist-packages (3.1.5)\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.49.1-py3-none-any.whl.metadata (9.5 kB)\n",
            "Collecting pyngrok\n",
            "  Downloading pyngrok-7.3.0-py3-none-any.whl.metadata (8.1 kB)\n",
            "Requirement already satisfied: langchain-core<1.0.0,>=0.3.72 in /usr/local/lib/python3.12/dist-packages (from langchain) (0.3.74)\n",
            "Requirement already satisfied: langchain-text-splitters<1.0.0,>=0.3.9 in /usr/local/lib/python3.12/dist-packages (from langchain) (0.3.9)\n",
            "Requirement already satisfied: langsmith>=0.1.17 in /usr/local/lib/python3.12/dist-packages (from langchain) (0.4.16)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in /usr/local/lib/python3.12/dist-packages (from langchain) (2.11.7)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.12/dist-packages (from langchain) (2.0.43)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.12/dist-packages (from langchain) (2.32.4)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.12/dist-packages (from langchain) (6.0.2)\n",
            "Collecting langgraph-checkpoint<3.0.0,>=2.1.0 (from langgraph)\n",
            "  Downloading langgraph_checkpoint-2.1.1-py3-none-any.whl.metadata (4.2 kB)\n",
            "Collecting langgraph-prebuilt<0.7.0,>=0.6.0 (from langgraph)\n",
            "  Downloading langgraph_prebuilt-0.6.4-py3-none-any.whl.metadata (4.5 kB)\n",
            "Collecting langgraph-sdk<0.3.0,>=0.2.2 (from langgraph)\n",
            "  Downloading langgraph_sdk-0.2.5-py3-none-any.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: xxhash>=3.5.0 in /usr/local/lib/python3.12/dist-packages (from langgraph) (3.5.0)\n",
            "Requirement already satisfied: numpy>=1.26.0 in /usr/local/lib/python3.12/dist-packages (from pandas) (2.0.2)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: et-xmlfile in /usr/local/lib/python3.12/dist-packages (from openpyxl) (2.0.0)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.2.1)\n",
            "Requirement already satisfied: packaging<26,>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.5.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.45)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.2.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.12/dist-packages (from langchain-core<1.0.0,>=0.3.72->langchain) (1.33)\n",
            "Collecting ormsgpack>=1.10.0 (from langgraph-checkpoint<3.0.0,>=2.1.0->langgraph)\n",
            "  Downloading ormsgpack-1.10.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (43 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m43.7/43.7 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: httpx>=0.25.2 in /usr/local/lib/python3.12/dist-packages (from langgraph-sdk<0.3.0,>=0.2.2->langgraph) (0.28.1)\n",
            "Requirement already satisfied: orjson>=3.10.1 in /usr/local/lib/python3.12/dist-packages (from langgraph-sdk<0.3.0,>=0.2.2->langgraph) (3.11.2)\n",
            "Requirement already satisfied: requests-toolbelt>=1.0.0 in /usr/local/lib/python3.12/dist-packages (from langsmith>=0.1.17->langchain) (1.0.0)\n",
            "Requirement already satisfied: zstandard>=0.23.0 in /usr/local/lib/python3.12/dist-packages (from langsmith>=0.1.17->langchain) (0.24.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.33.2 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (2.33.2)\n",
            "Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.4.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2->langchain) (3.4.3)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2->langchain) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2->langchain) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2->langchain) (2025.8.3)\n",
            "Requirement already satisfied: greenlet>=1 in /usr/local/lib/python3.12/dist-packages (from SQLAlchemy<3,>=1.4->langchain) (3.2.4)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.12/dist-packages (from httpx>=0.25.2->langgraph-sdk<0.3.0,>=0.2.2->langgraph) (4.10.0)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.12/dist-packages (from httpx>=0.25.2->langgraph-sdk<0.3.0,>=0.2.2->langgraph) (1.0.9)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.12/dist-packages (from httpcore==1.*->httpx>=0.25.2->langgraph-sdk<0.3.0,>=0.2.2->langgraph) (0.16.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.12/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<1.0.0,>=0.3.72->langchain) (3.0.0)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.4.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.27.0)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.12/dist-packages (from anyio->httpx>=0.25.2->langgraph-sdk<0.3.0,>=0.2.2->langgraph) (1.3.1)\n",
            "Downloading langgraph-0.6.6-py3-none-any.whl (153 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m153.3/153.3 kB\u001b[0m \u001b[31m10.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading streamlit-1.49.1-py3-none-any.whl (10.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m10.0/10.0 MB\u001b[0m \u001b[31m40.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pyngrok-7.3.0-py3-none-any.whl (25 kB)\n",
            "Downloading langgraph_checkpoint-2.1.1-py3-none-any.whl (43 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m43.9/43.9 kB\u001b[0m \u001b[31m2.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langgraph_prebuilt-0.6.4-py3-none-any.whl (28 kB)\n",
            "Downloading langgraph_sdk-0.2.5-py3-none-any.whl (54 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m54.1/54.1 kB\u001b[0m \u001b[31m2.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m40.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading ormsgpack-1.10.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (216 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m216.7/216.7 kB\u001b[0m \u001b[31m12.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: pyngrok, ormsgpack, pydeck, langgraph-sdk, streamlit, langgraph-checkpoint, langgraph-prebuilt, langgraph\n",
            "Successfully installed langgraph-0.6.6 langgraph-checkpoint-2.1.1 langgraph-prebuilt-0.6.4 langgraph-sdk-0.2.5 ormsgpack-1.10.0 pydeck-0.9.1 pyngrok-7.3.0 streamlit-1.49.1\n"
          ]
        }
      ],
      "source": [
        "!pip install langchain langgraph pandas openpyxl streamlit pyngrok\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "It2Ouk-XgLMM",
        "outputId": "fcb5746b-1ebb-4ddc-b4aa-f6d4c48145eb"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Patients: (50, 13)\n",
            "Doctors: (168, 6)\n",
            "Appointments: (0, 15)\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "patients_df = pd.read_csv(\"patients.csv\")\n",
        "doctors_df = pd.read_excel(\"doctors.xlsx\")\n",
        "appointments_df = pd.read_excel(\"appointments.xlsx\")\n",
        "\n",
        "print(\"Patients:\", patients_df.shape)\n",
        "print(\"Doctors:\", doctors_df.shape)\n",
        "print(\"Appointments:\", appointments_df.shape)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ZAsw2XfxgY4b"
      },
      "outputs": [],
      "source": [
        "from datetime import datetime\n",
        "\n",
        "def lookup_patient(name, dob):\n",
        "    match = patients_df[(patients_df[\"first_name\"]==name) & (patients_df[\"dob\"]==dob)]\n",
        "    return match.iloc[0] if not match.empty else None\n",
        "\n",
        "def get_available_slots(doctor, date, duration):\n",
        "    slots = doctors_df[\n",
        "        (doctors_df[\"doctor\"]==doctor) &\n",
        "        (doctors_df[\"date\"]==date) &\n",
        "        (doctors_df[\"is_available\"])\n",
        "    ]\n",
        "    return slots.head(5)\n",
        "\n",
        "def book_appointment(patient, doctor, date, start, duration, insurance):\n",
        "    global appointments_df\n",
        "    appt_id = len(appointments_df) + 1\n",
        "    end_hour = int(start.split(\":\")[0]) + duration//60\n",
        "    appointments_df.loc[len(appointments_df)] = [\n",
        "        appt_id, patient[\"patient_id\"], f\"{patient['first_name']} {patient['last_name']}\",\n",
        "        doctor, date, start, f\"{end_hour}:00\",\n",
        "        \"new\" if not patient[\"is_returning\"] else \"returning\",\n",
        "        bool(insurance), \"confirmed\", \"\", \"\", \"\", \"\", \"None\"\n",
        "    ]\n",
        "    appointments_df.to_excel(\"appointments.xlsx\", index=False)\n",
        "    return appt_id\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u7gzddgagcd5",
        "outputId": "1664c312-a4d2-48fd-d3c7-5a14519bc5d4"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "New patient\n",
            "Available Slots:\n",
            "   doctor        date slot_start slot_end  location  is_available\n",
            "0  Dr. A  2025-09-03       9:00    10:00  New York          True\n",
            "1  Dr. A  2025-09-03      10:00    11:00   Chicago          True\n",
            "2  Dr. A  2025-09-03      11:00    12:00  New York          True\n",
            "3  Dr. A  2025-09-03      12:00    13:00   Chicago          True\n",
            "4  Dr. A  2025-09-03      13:00    14:00  New York          True\n",
            "✅ Appointment confirmed with ID 1\n"
          ]
        }
      ],
      "source": [
        "name, dob = \"Patient1\", \"2016-03-13\"\n",
        "patient = lookup_patient(name, dob)\n",
        "\n",
        "if patient is not None:\n",
        "    print(\"Returning patient\" if patient[\"is_returning\"] else \"New patient\")\n",
        "else:\n",
        "    print(\"New patient\")\n",
        "\n",
        "slots = get_available_slots(\"Dr. A\", datetime.today().strftime(\"%Y-%m-%d\"), 60)\n",
        "print(\"Available Slots:\\n\", slots)\n",
        "\n",
        "appt_id = book_appointment(patient, \"Dr. A\", datetime.today().strftime(\"%Y-%m-%d\"), \"10:00\", 60, {\"carrier\":\"Aetna\"})\n",
        "print(f\"✅ Appointment confirmed with ID {appt_id}\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5GGclV5sgfpI",
        "outputId": "019615cd-d2d0-4367-a068-596865187e45"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "2025-09-03 16:56:30.613 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.858 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-09-03 16:56:30.862 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.865 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.869 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.874 Session state does not function when running a script without `streamlit run`\n",
            "2025-09-03 16:56:30.880 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.884 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.887 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.892 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.899 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.900 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.905 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.907 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.910 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.911 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.911 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.912 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.913 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.914 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.914 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.915 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.915 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.916 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.917 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.918 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.918 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.919 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.920 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.920 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-09-03 16:56:30.921 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "from datetime import datetime\n",
        "\n",
        "patients_df = pd.read_csv(\"patients.csv\")\n",
        "doctors_df = pd.read_excel(\"doctors.xlsx\")\n",
        "appointments_df = pd.read_excel(\"appointments.xlsx\")\n",
        "\n",
        "st.title(\"AI Appointment Scheduler Chatbot\")\n",
        "\n",
        "if \"step\" not in st.session_state:\n",
        "    st.session_state.step = 0\n",
        "    st.session_state.patient = None\n",
        "\n",
        "if st.session_state.step == 0:\n",
        "    name = st.text_input(\"Enter your first name:\")\n",
        "    dob = st.text_input(\"Enter your date of birth (YYYY-MM-DD):\")\n",
        "    if st.button(\"Continue\"):\n",
        "        patient = patients_df[(patients_df[\"first_name\"]==name) & (patients_df[\"dob\"]==dob)]\n",
        "        if not patient.empty:\n",
        "            st.session_state.patient = patient.iloc[0]\n",
        "            st.success(\"Welcome back! Returning patient.\")\n",
        "        else:\n",
        "            st.session_state.patient = {\"first_name\": name, \"dob\": dob, \"is_returning\": False}\n",
        "            st.success(\"Welcome! New patient.\")\n",
        "        st.session_state.step = 1\n",
        "\n",
        "elif st.session_state.step == 1:\n",
        "    doctor = st.selectbox(\"Choose your doctor:\", doctors_df[\"doctor\"].unique())\n",
        "    date = st.selectbox(\"Choose appointment date:\", doctors_df[\"date\"].unique())\n",
        "    duration = 30 if st.session_state.patient[\"is_returning\"] else 60\n",
        "    slots = doctors_df[(doctors_df[\"doctor\"]==doctor) & (doctors_df[\"date\"]==date)]\n",
        "    slot = st.selectbox(\"Choose time slot:\", slots[\"slot_start\"].unique())\n",
        "    carrier = st.text_input(\"Insurance Carrier:\")\n",
        "    member = st.text_input(\"Member ID:\")\n",
        "    group = st.text_input(\"Group Number:\")\n",
        "\n",
        "    if st.button(\"Confirm Appointment\"):\n",
        "        appt_id = len(appointments_df) + 1\n",
        "        appointments_df.loc[len(appointments_df)] = [\n",
        "            appt_id, \"ID\", f\"{st.session_state.patient['first_name']} Test\", doctor,\n",
        "            date, slot, f\"{int(slot.split(':')[0]) + duration//60}:00\",\n",
        "            \"new\" if not st.session_state.patient[\"is_returning\"] else \"returning\",\n",
        "            True, \"confirmed\", \"\", \"\", \"\", \"\", \"None\"\n",
        "        ]\n",
        "        appointments_df.to_excel(\"appointments.xlsx\", index=False)\n",
        "        st.success(f\"✅ Appointment confirmed! Your ID is {appt_id}\")\n",
        "        st.session_state.step = 2\n",
        "\n",
        "elif st.session_state.step == 2:\n",
        "    st.info(\"📄 Intake form will be sent to your email.\")\n",
        "    st.write(\"Your appointment is saved. You’ll also get reminders.\")\n",
        "    st.dataframe(appointments_df.tail(5))\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN8pGqPk8i7UGtnFFXCH8y+",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}