// Fill out your copyright notice in the Description page of Project Settings.


#include "GameInstance_webSocket.h"
#include "WebSocketsModule.h"
#include <Kismet/GameplayStatics.h>


void UGameInstance_webSocket::Init()
{
	Super::Init();

	if (!FModuleManager::Get().IsModuleLoaded("WebSockets"))
	{
		FModuleManager::Get().LoadModule("WebSockets");
	}
	WebSocket = FWebSocketsModule::Get().CreateWebSocket("wss://31ok2x42e4.execute-api.ap-northeast-1.amazonaws.com/production");

	WebSocket->OnConnected().AddLambda([]()
		{
			GEngine->AddOnScreenDebugMessage(-1, 15.0f, FColor::Green, "successfully connected");
		});
	WebSocket->OnConnectionError().AddLambda([](const FString& Error)
		{
			GEngine->AddOnScreenDebugMessage(-1, 15.0f, FColor::Green, Error);
		});
	WebSocket->OnClosed().AddLambda([](int32 StatusCode, const FString& Reason, bool bWasClean)
		{
			GEngine->AddOnScreenDebugMessage(-1, 15.0f, bWasClean ? FColor::Green : FColor::Red, "connection closed" + Reason);
		});
	WebSocket->OnMessage().AddLambda([=](const FString& MessageString)
		{
			//x = "sj";
			call_function_for_movement(MessageString);

			GEngine->AddOnScreenDebugMessage(-1, 15.0f, FColor::Cyan, "Received message: " + MessageString);
			
		
		

		});
	WebSocket->OnMessageSent().AddLambda([](const FString& MessageString)
		{
			GEngine->AddOnScreenDebugMessage(-1, 15.0f, FColor::Yellow, "sent message: " + MessageString);
		});
	WebSocket->Connect();
}
void UGameInstance_webSocket::Shutdown()
{
	if (WebSocket->IsConnected())
	{
		WebSocket->Close();
	}
	Super::Shutdown();
}


void UGameInstance_webSocket::call_function_for_movement(const FString& message) {
	characterpointer = Cast<AMyProjectCharacter>(UGameplayStatics::GetPlayerCharacter(GetWorld(), 0));
	UE_LOG(LogTemp, Warning, TEXT("Some location message"));
	float MyShinyNewFloat = FCString::Atof(*message);
	characterpointer->MoveForward(MyShinyNewFloat);
}
