CREATE TABLE "User_" (
  "UserId" SERIAL PRIMARY KEY,
  "Name" text,
  "GroupNameOveride" text
);

CREATE TABLE "Group_" (
  "GroupId" SERIAL PRIMARY KEY,
  "Name" text,
  "Description" text,
  "Icon" text,
  "User" int,
  FOREIGN KEY ("User") REFERENCES "User_" ("UserId")
);

CREATE TABLE "Client_" (
  "ClientId" SERIAL PRIMARY KEY,
  "Name" text,
  "Description" text,
  "Icon" text,
  "Group_" int,
  "FilePath" text,
  ADD FOREIGN KEY ("Group_") REFERENCES "Group_" ("GroupId")
);

CREATE TABLE "Project_" (
  "ProjectId" SERIAL PRIMARY KEY,
  "Name" text,
  "Description" text,
  "Icon" text,
  "ProjectType" text,
  "Client" int,
  "Delivery" blob,
  "Status" int,
  "FilePath" text,
  ADD FOREIGN KEY ("Client") REFERENCES "Client_" ("ClientId")
);

CREATE TABLE "Scene_" (
  "id" SERIAL PRIMARY KEY,
  "SceneID" text,
  "Version" text,
  "Project" int,
  "Exports" int,
  ADD FOREIGN KEY ("Project") REFERENCES "Project_" ("ProjectId")
);

CREATE TABLE "ShotFile_" (
  "id" SERIAL PRIMARY KEY,
  "FilePath" text,
  "SoftwarePackage" timestamp,
  "RenderEngine" int,
  "Shot" int,
  "Exports" int,
  ADD FOREIGN KEY ("Shot") REFERENCES "Shot_" ("id")
);

CREATE TABLE "Shot_" (
  "id" SERIAL PRIMARY KEY,
  "ShotID" text,
  "FullID" text,
  "Version" text,
  "Scene" int,
  "EditFile" int,
  "MainShotFile" int,
  ADD FOREIGN KEY ("Scene") REFERENCES "Scene_" ("id"),

ADD FOREIGN KEY ("MainShotFile") REFERENCES "ShotFile_" ("id"),

ADD FOREIGN KEY ("EditFile") REFERENCES "EditFileLoadedShots_" ("id")
);

CREATE TABLE "EditFile_" (
  "id" SERIAL PRIMARY KEY,
  "FilePath" text,
  "Version" text,
  "SoftwarePackage" int,
  "Project" int,
  "Exports" int,
  ADD FOREIGN KEY ("Project") REFERENCES "Project_" ("ProjectId"),

ADD FOREIGN KEY ("Exports") REFERENCES "Exports_" ("id")
);

CREATE TABLE "EditFileLoadedShots_" (
  "id" SERIAL PRIMARY KEY,
  "EditFile" int
);

CREATE TABLE "Camera_" (
  "id" SERIAL PRIMARY KEY,
  "CameraName" text,
  "Resolution" text,
  "Version" text,
  "Scene" int,
  "MainShotFile" int,
  "Exports" int
);

CREATE TABLE "SavedCameraPath_" (
  "id" SERIAL PRIMARY KEY,
  "Filepath" text,
  "Camera" int,
  ADD FOREIGN KEY ("Camera") REFERENCES "Camera_" ("id")
);

CREATE TABLE "CameraKeyframe_" (
  "id" SERIAL PRIMARY KEY,
  "CameraKeyframeList" int,
  "Frame" text,
  "Interpolation" text,
  "PixelAspectRatio" int,
  "Projection" text,
  "FocalLength" int,
  "FilmBack" text,
  "ShutterTime" text,
  "FocusDistance" text,
  "Fstop" text,
  "Bokeh" text,
  "BackgroundImage" text,
  "Transform" int,
  ADD FOREIGN KEY ("Transform") REFERENCES "Transform_" ("id"),

ADD FOREIGN KEY ("CameraKeyframeList") REFERENCES "CameraKeyframeList_" ("id")
);

CREATE TABLE "CameraKeyframeList_" (
  "id" SERIAL PRIMARY KEY,
  "Camera" int,
  ADD FOREIGN KEY ("Camera") REFERENCES "Camera_" ("id")
);

CREATE TABLE "Transform_" (
  "id" SERIAL PRIMARY KEY,
  "Position" text,
  "RotationEuler" text,
  "RotationQuaternion" int,
  "Scale" text
);

CREATE TABLE "TransformKeyframe_" (
  "id" SERIAL PRIMARY KEY,
  "Frame" int,
  "Interpolation" text,
  "Transform" int,
  ADD FOREIGN KEY ("Transform") REFERENCES "Transform_" ("id")
);

CREATE TABLE "RenderEngine_" (
  "id" SERIAL PRIMARY KEY,
  "Filepath" text,
  "RenderEngineName" text,
  "Type" text,
  "CommandArguments" text,
  "Description" text
);

CREATE TABLE "SoftwarePackage_" (
  "id" SERIAL PRIMARY KEY,
  "Filepath" text,
  "SoftwareName" text,
  "Type" text,
  "CommandArguments" text,
  "Description" text
);

CREATE TABLE "Exports_" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "ExportedFile_" (

);

CREATE TABLE "PreviewExport_" (

);

CREATE TABLE "FinalExport_" (

);

CREATE TABLE "Delivery_" (

);

CREATE TABLE "DeliveryFiles_" (
);

CREATE TABLE "DeliveryFile_" (

);

CREATE TABLE "PostPipeline" (

);

CREATE TABLE "PostPipelineSettings" (

);

CREATE TABLE "PostPipelineDependencies_" (

);







